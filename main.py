from utilities.notifications import send_notification
from utilities.statistics import get_affiliate_statistics

import time
import asyncio
from datetime import datetime

def main():
    asyncio.run(send_notification("🟢 App online"))
    previous_available_bonus_balance, previous_unsettled_amount, previous_bonus_earned, previous_number_of_invited, previous_recommended_order = 0, 0, 0, 0, 0
    previous_total_amount = 0
    
    available_bonus_balance, unsettled_amount, bonus_earned, number_of_invited, recommended_order = get_affiliate_statistics()
    print("[>] First run")
    total_amount = available_bonus_balance + unsettled_amount

    now = datetime.now()

    notification_message = """
    ⬇️ Current Stats (At Start) ⬇️ {}\n
    💵 Available Bonus Balance: ${}\n
    💸 Unsettled Amount: ${}\n
    🤑 Total Amount: ${}\n
    🎉 Bonus Earned: ${}\n
    🧑‍🤝‍🧑 Number of Invited: {}\n
    📈 Recommended Order: {}
    """.format(
        (now.hour, now.day, now.month),
        available_bonus_balance,
        unsettled_amount,
        total_amount,
        bonus_earned,
        number_of_invited,
        recommended_order,
        )

    asyncio.run(send_notification(notification_message))

    while True:
        print("[>] Looooop!")

        available_bonus_balance, unsettled_amount, bonus_earned, number_of_invited, recommended_order = get_affiliate_statistics()
        total_amount = available_bonus_balance + unsettled_amount

        available_bonus_balance_difference, unsettled_amount_difference, bonus_earned_difference, number_of_invited_difference, recommended_order_difference = available_bonus_balance-previous_available_bonus_balance, unsettled_amount-previous_unsettled_amount, bonus_earned-previous_bonus_earned, number_of_invited-previous_number_of_invited, recommended_order-previous_recommended_order
        total_amount_difference = total_amount - previous_total_amount

        print("[>] Sending message")

        now = datetime.now()

        notification_message = """
        ⬇️ Last Hour ⬇️ {}
        💵 Available Bonus Balance: ${} (${})\n
        💸 Unsettled Amount: ${} (${})\n
        🤑 Total Amount: ${} (${})\n
        🎉 Bonus Earned: ${} (${})\n
        🧑‍🤝‍🧑 Number of Invited: {} ({})\n
        📈 Recommended Order: {} ({})
        """.format(
            (now.hour, now.day, now.month),
            available_bonus_balance,
            available_bonus_balance_difference,
            unsettled_amount,
            unsettled_amount_difference,
            total_amount,
            total_amount_difference,
            bonus_earned,
            bonus_earned_difference,
            number_of_invited,
            number_of_invited_difference,
            recommended_order,
            recommended_order_difference
            )

        asyncio.run(send_notification(notification_message))

        previous_available_bonus_balance, previous_unsettled_amount, previous_bonus_earned, previous_number_of_invited, previous_recommended_order = available_bonus_balance, unsettled_amount, bonus_earned, number_of_invited, recommended_order
        previous_total_amount = total_amount

        time.sleep(3600)

if __name__ == '__main__':
    print("[>] Starting application")

    main()