import asyncio
from datetime import datetime, timedelta
import json

from utilities.notifications import send_notification
from utilities.statistics import get_affiliate_statistics

def store_statistics(stats):
    filename = "statistics_data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(stats)
    with open(filename, "w") as file:
        json.dump(data, file)

def get_previous_statistics():
    filename = "statistics_data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if data and len(data) > 1:
                return data[-2]  # Return the second last recorded stats to compare with the last one
    except FileNotFoundError:
        pass
    return None

async def wait_until_next_hour():
    now = datetime.now()
    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    wait_seconds = (next_hour - now).total_seconds()
    await asyncio.sleep(wait_seconds)

async def main():
    await send_notification("🟢 App online")

    while True:
        now = datetime.now()
        previous_stats = get_previous_statistics()

        current_stats = get_affiliate_statistics()
        total_amount = current_stats[0] + current_stats[1]  # Assuming these are available_bonus_balance and unsettled_amount

        stats = {
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
            "available_bonus_balance": current_stats[0],
            "unsettled_amount": current_stats[1],
            "total_amount": total_amount,
            "bonus_earned": current_stats[2],
            "number_of_invited": current_stats[3],
            "recommended_order": current_stats[4]
        }
        store_statistics(stats)

        # Define which stats are monetary for appropriate formatting
        monetary_stats = ["available_bonus_balance", "unsettled_amount", "total_amount", "bonus_earned"]
        
        # Prepare the differences for notification
        if previous_stats:
            diffs = {key: stats[key] - previous_stats.get(key, 0) for key in stats if key not in ['timestamp']}
            diffs_message = []
            for key in diffs:
                if key in monetary_stats:
                    value_format = f"{key.replace('_', ' ').title()}: ${stats[key]} (${'+{:.2f}'.format(diffs[key]) if diffs[key] >= 0 else '{:.2f}'.format(diffs[key])})"
                else:
                    value_format = f"{key.replace('_', ' ').title()}: {stats[key]} ({'+{}'.format(diffs[key]) if diffs[key] >= 0 else '{}'.format(diffs[key])})"
                diffs_message.append(value_format)
            diffs_message = "\n".join(diffs_message)
        else:
            diffs_message = "\n".join(f"{key.replace('_', ' ').title()}: ${stats[key]}" if key in monetary_stats else f"{key.replace('_', ' ').title()}: {stats[key]}" for key in stats if key not in ['timestamp'])

        notification_message = f"⬇️ Stats for {now.strftime('%Y-%m-%d %H:%M')} ⬇️\n{diffs_message}"
        await send_notification(notification_message)

        # Wait until the next hour to run again
        await wait_until_next_hour()

if __name__ == '__main__':
    print("[>] Starting application")
    asyncio.run(main())