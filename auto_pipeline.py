import os
from playwright.sync_api import sync_playwright
from datetime import datetime

EMAIL = os.getenv("NOTE_EMAIL")
PASSWORD = os.getenv("NOTE_PASSWORD")

def create_draft(title, body):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("noteへアクセス")
        page.goto("https://note.com/login")

        print("ログイン方法選択待機")
        page.wait_for_selector('button:has-text("メールアドレスでログイン")', timeout=15000)
        page.click('button:has-text("メールアドレスでログイン")')

        print("メール欄待機")
        page.wait_for_selector('input[type="email"]', timeout=15000)

        print("ログイン処理")
        page.fill('input[type="email"]', EMAIL)
        page.fill('input[type="password"]', PASSWORD)
        page.click('button[type="submit"]')

        page.wait_for_load_state("networkidle")

        print("記事作成画面へ")
        page.goto("https://note.com/notes/new")
        page.wait_for_load_state("networkidle")

        print("タイトル入力")
        page.fill('textarea', title)

        print("本文入力")
        page.fill('[contenteditable="true"]', body)

        print("下書き保存")
        page.keyboard.press("Control+S")

        page.wait_for_timeout(3000)
        browser.close()


def main():
    now = datetime.now()
    title = f"テスト投稿 {now}"
    body = "健闘を祈る"

    create_draft(title, body)
    print("完了")


if __name__ == "__main__":
    main()
