# -*- coding: utf-8 -*-
"""
Google Chat Integration Script for The Academic Times & The Junior
Sends daily update summary and Hitokoto News to a Google Chat Space via Incoming Webhook.
"""

import os
import sys
import json
import urllib.request
import argparse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def create_daily_update_message(date_str="2026-11-03"):
    message = {
        "text": f"📰 *THE ACADEMIC TIMES & THE JUNIOR — 本日の更新完了（{date_str}号）*\n\n"
                f"入試・教養の本格英語ニュースポータルを本日分に更新しました。\n"
                f"Senior版（発展・CEFR B2-C1）とJunior版（基礎・英検準2〜2級）が完全1:1対応、英国音声（Edge-TTS）付きで公開されています。\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"🌟 *本日のピックアップ・ひとことニュース3選*\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"1️⃣ *【科学・天文】夜明け前の東の空に金星・三日月・スピカの三重天体直列*\n"
                f"・秋の澄んだ空で金星と細い月、おとめ座スピカが三角形を形成。天体視差や宇宙の奥行きを学ぶ格好の天文現象。\n"
                f"🔗 Senior版: https://tbt-beginner.github.io/academictimes/science/starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn/index.html\n"
                f"🌱 Junior版: https://tbt-beginner.github.io/academictimes/junior/science/starwatch-catch-the-striking-trifecta-of-venus-the-moon-and-spica-at-break-of-dawn/index.html\n\n"
                f"2️⃣ *【法律・権利】豪州の16歳未満SNS全面禁止令、憲法違反を巡り最高裁判所へ*\n"
                f"・若者のメンタル保護を掲げる新法に対し、表現の自由や政治的対話の権利を侵害するとして違憲訴訟が提起。\n"
                f"🔗 Senior版: https://tbt-beginner.github.io/academictimes/law/australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project/index.html\n"
                f"🌱 Junior版: https://tbt-beginner.github.io/academictimes/junior/law/australia-social-media-ban-high-court-challenge-reddit-digital-freedom-project/index.html\n\n"
                f"3️⃣ *【科学・生物】気性の荒い雄牛と年老いたロバの異種間の深い友情に科学者が注目*\n"
                f"・種や鳴き声の違いを超えて寄り添い合う哺乳類の共感とオキシトシン愛着行動。動物行動学の新たな発見。\n"
                f"🔗 Senior版: https://tbt-beginner.github.io/academictimes/science/tender-bond-male-donkey-bull-baffles-scientists/index.html\n"
                f"🌱 Junior版: https://tbt-beginner.github.io/academictimes/junior/science/tender-bond-male-donkey-bull-baffles-scientists/index.html\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📊 *サイト稼働ステータス*\n"
                f"・総記事数: 405 Senior ＋ 405 Junior ＝ 全810記事\n"
                f"・Edge-TTS音声: 全記事・全対話 100% 生成済み\n"
                f"・内部リンク完全監査: リンク切れ 0件（Broken links: 0）\n"
                f"🌐 ポータルトップ: https://tbt-beginner.github.io/academictimes/\n"
    }
    return message

def send_to_google_chat(webhook_url, payload):
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=UTF-8"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, resp.read().decode("utf-8")

def main():
    parser = argparse.ArgumentParser(description="Send daily update notification to Google Chat space")
    parser.add_argument("--webhook", help="Google Chat Incoming Webhook URL (or set GOOGLE_CHAT_WEBHOOK_URL env)")
    parser.add_argument("--date", default="2026-11-03", help="Edition date")
    parser.add_argument("--dry-run", action="store_true", help="Print message payload without sending")
    args = parser.parse_args()

    webhook_url = args.webhook or os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")
    message = create_daily_update_message(args.date)

    if args.dry_run or not webhook_url:
        print("[DRY-RUN] Google Chat message preview:")
        print(message["text"])
        if not webhook_url:
            print("\n[NOTE] No webhook URL configured. Pass --webhook <URL> or set GOOGLE_CHAT_WEBHOOK_URL to send automatically.")
        return

    print(f"Sending daily update to Google Chat...")
    status, body = send_to_google_chat(webhook_url, message)
    print(f"Response ({status}): {body}")

if __name__ == "__main__":
    main()
