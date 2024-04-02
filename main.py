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

def calculate_totals_for_period(start_date, end_date):
    filename = "statistics_data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Statistics file not found.")
        return

    total_money = sum(item['total_amount'] for item in data if start_date <= datetime.strptime(item['timestamp'], "%Y-%m-%d %H:%M:%S") <= end_date)
    return total_money

def get_previous_statistics():
    filename = "statistics_data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if data:
                return data[-1]  # Return the last recorded stats
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

        available_bonus_balance, unsettled_amount, bonus_earned, number_of_invited, recommended_order = get_affiliate_statistics()
        total_amount = available_bonus_balance + unsettled_amount

        stats = {
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
            "available_bonus_balance": available_bonus_balance,
            "unsettled_amount": unsettled_amount,
            "total_amount": total_amount,
            "bonus_earned": bonus_earned,
            "number_of_invited": number_of_invited,
            "recommended_order": recommended_order
        }
        store_statistics(stats)

        if previous_stats:
            diff = {key: stats[key] - previous_stats.get(key, 0) for key in stats if key not in ['timestamp', 'recommended_order']}
            diff_message = "\n".join(f"{key}: ${stats[key]} (${diff[key]})" for key in diff)
            recommended_order_diff = stats['recommended_order'] - previous_stats.get('recommended_order', 0)
        else:
            diff_message = "\n".join(f"{key}: ${stats[key]}" for key in stats if key not in ['timestamp', 'recommended_order'])
            recommended_order_diff = stats['recommended_order']

        notification_message = f"""
        ⬇️ Stats for {now.strftime('%Y-%m-%d %H:%M')} ⬇️\n{diff_message}\n
        📈 Recommended Order: {stats['recommended_order']} ({recommended_order_diff})
        """
        await send_notification(notification_message)

        # Wait until the next hour to run again
        await wait_until_next_hour()

if __name__ == '__main__':
    print("[>] Starting application")
    asyncio.run(main())