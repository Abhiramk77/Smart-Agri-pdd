#!/usr/bin/env python3
"""
Flutter App Demo - Generates visual demonstration of Smart Agri App
Shows login, dashboard, contracts, messaging, and settings screens
"""

import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
from datetime import datetime

def create_flutter_app_screens():
    """Create visual representation of Flutter app screens"""

    # Screen dimensions (mobile size: 1080x1920)
    WIDTH = 1080
    HEIGHT = 1920

    def create_splash_screen():
        """Create splash/loading screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#2D5016')  # Farm green
        draw = ImageDraw.Draw(img)

        # Draw title
        title = "SMART AGRI"
        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 120)
            font_subtitle = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
        except:
            font_title = ImageFont.load_default()
            font_subtitle = ImageFont.load_default()

        # Center text
        bbox = draw.textbbox((0, 0), title, font=font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((WIDTH - title_width) // 2, 800), title, fill='white', font=font_title)

        # Subtitle
        bbox = draw.textbbox((0, 0), "Agricultural Contract Platform", font=font_subtitle)
        subtitle_width = bbox[2] - bbox[0]
        draw.text(((WIDTH - subtitle_width) // 2, 950), "Agricultural Contract Platform",
                 fill='#90EE90', font=font_subtitle)

        # Loading indicator
        draw.ellipse([(450, 1400), (630, 1580)], outline='white', width=5)
        draw.text(((WIDTH - 150) // 2, 1650), "Loading...", fill='white', font=font_subtitle)

        return img

    def create_login_screen():
        """Create login screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#F5F5F5')
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 60)
            font_text = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 32)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()

        # Title
        draw.text((100, 200), "Welcome Back", fill='#2D5016', font=font_title)

        # Email field
        draw.rectangle([(100, 400), (980, 500)], fill='white', outline='#CCCCCC', width=2)
        draw.text((120, 420), "Email", fill='#666666', font=font_text)
        draw.text((120, 450), "farmer@farming.com", fill='#999999', font=font_text)

        # Password field
        draw.rectangle([(100, 550), (980, 650)], fill='white', outline='#CCCCCC', width=2)
        draw.text((120, 570), "Password", fill='#666666', font=font_text)
        draw.text((120, 600), "••••••••••", fill='#999999', font=font_text)

        # Sign In button
        draw.rectangle([(100, 750), (980, 850)], fill='#2D5016', width=0)
        bbox = draw.textbbox((0, 0), "SIGN IN", font=font_title)
        btn_text_width = bbox[2] - bbox[0]
        draw.text(((WIDTH - btn_text_width) // 2, 770), "SIGN IN", fill='white', font=font_title)

        # Sign up link
        draw.text(((WIDTH - 300) // 2, 950), "Don't have account? SIGN UP", fill='#2D5016', font=font_text)

        return img

    def create_dashboard():
        """Create dashboard/home screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#FFFFFF')
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 50)
            font_text = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30)
            font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 24)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Header
        draw.rectangle([(0, 0), (WIDTH, 200)], fill='#2D5016', width=0)
        draw.text((50, 50), "Hello, John!", fill='white', font=font_title)
        draw.text((50, 110), "Farmer • California", fill='#90EE90', font=font_small)

        # Statistics cards
        cards_y = 250

        # Active Contracts
        draw.rectangle([(50, cards_y), (500, cards_y + 120)], fill='#90EE90', width=0)
        draw.text((70, cards_y + 20), "Active Contracts", fill='#2D5016', font=font_text)
        draw.text((70, cards_y + 60), "2", fill='#2D5016', font=font_title)

        # Pending Offers
        draw.rectangle([(580, cards_y), (1030, cards_y + 120)], fill='#FFD700', width=0)
        draw.text((600, cards_y + 20), "Pending Offers", fill='#2D5016', font=font_text)
        draw.text((600, cards_y + 60), "5", fill='#2D5016', font=font_title)

        # Quick Actions
        draw.text((50, cards_y + 200), "Quick Actions", fill='#2D5016', font=font_title)

        # Browse Marketplace button
        draw.rectangle([(50, cards_y + 280), (500, cards_y + 380)], fill='#4CAF50', width=0)
        draw.text((70, cards_y + 310), "📊 Browse Marketplace", fill='white', font=font_text)

        # View Messages button
        draw.rectangle([(580, cards_y + 280), (1030, cards_y + 380)], fill='#2196F3', width=0)
        draw.text((600, cards_y + 310), "💬 Messages", fill='white', font=font_text)

        # Recent Activity
        draw.text((50, cards_y + 420), "Recent Activity", fill='#2D5016', font=font_title)

        # Activities
        activities = [
            ("Fresh Foods Co. accepted your offer", "2 hours ago"),
            ("New contract: Organic Tomatoes", "4 hours ago"),
            ("Payment received: ₹1,250", "1 day ago")
        ]

        y_offset = cards_y + 500
        for activity, time in activities:
            draw.text((50, y_offset), activity, fill='#333333', font=font_small)
            draw.text((50, y_offset + 35), time, fill='#999999', font=font_small)
            y_offset += 90

        # Bottom navigation (simulate)
        draw.rectangle([(0, HEIGHT - 120), (WIDTH, HEIGHT)], fill='#F5F5F5', width=0)
        nav_items = ["🏠 Home", "📋 Contracts", "💬 Chat", "⚙️ Settings"]
        x_start = 50
        for item in nav_items:
            draw.text((x_start, HEIGHT - 80), item, fill='#2D5016', font=font_small)
            x_start += 250

        return img

    def create_contracts_screen():
        """Create contracts/marketplace screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#FFFFFF')
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 50)
            font_text = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 28)
            font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 22)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Header
        draw.rectangle([(0, 0), (WIDTH, 150)], fill='#2D5016', width=0)
        draw.text((50, 50), "Marketplace", fill='white', font=font_title)

        # Search/filter
        draw.rectangle([(50, 180), (1030, 250)], fill='#F5F5F5', outline='#CCCCCC', width=2)
        draw.text((70, 200), "🔍 Search by category...", fill='#999999', font=font_text)

        # Contracts list
        contracts = [
            {
                "title": "Organic Tomatoes",
                "seller": "Fresh Foods Co. ⭐ 4.8",
                "quantity": "500 kg • ₹2.50/kg",
                "price": "₹1,250",
                "img": "🍅"
            },
            {
                "title": "Atlantic Salmon",
                "seller": "Ocean Catch Inc. ⭐ 4.6",
                "quantity": "2000 lbs • ₹8.50/lb",
                "price": "₹17,000",
                "img": "🐟"
            },
            {
                "title": "Raw Milk",
                "seller": "Green Valley Dairy ⭐ 4.9",
                "quantity": "1000 L/week • ₹1.20/L",
                "price": "₹4,800/mo",
                "img": "🥛"
            }
        ]

        y_offset = 300
        for contract in contracts:
            # Contract card
            draw.rectangle([(50, y_offset), (1030, y_offset + 180)],
                          fill='#F9F9F9', outline='#E0E0E0', width=2)

            # Icon
            draw.text((70, y_offset + 20), contract["img"], fill='#2D5016', font=font_title)

            # Title
            draw.text((200, y_offset + 20), contract["title"], fill='#2D5016', font=font_text)

            # Seller
            draw.text((200, y_offset + 60), contract["seller"], fill='#666666', font=font_small)

            # Details
            draw.text((200, y_offset + 95), contract["quantity"], fill='#999999', font=font_small)

            # Price
            draw.text((200, y_offset + 130), contract["price"], fill='#2D5016', font=font_text)

            y_offset += 200

        # Bottom navigation
        draw.rectangle([(0, HEIGHT - 120), (WIDTH, HEIGHT)], fill='#F5F5F5', width=0)
        nav_items = ["🏠 Home", "📋 Contracts", "💬 Chat", "⚙️ Settings"]
        x_start = 50
        for idx, item in enumerate(nav_items):
            color = '#2D5016' if idx == 1 else '#999999'
            draw.text((x_start, HEIGHT - 80), item, fill=color, font=font_small)
            x_start += 250

        return img

    def create_chat_screen():
        """Create messaging/chat screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#FFFFFF')
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 50)
            font_text = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 28)
            font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 22)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Header
        draw.rectangle([(0, 0), (WIDTH, 150)], fill='#2D5016', width=0)
        draw.text((50, 50), "Messages", fill='white', font=font_title)

        # Chats list
        chats = [
            {
                "name": "Fresh Foods Co.",
                "message": "Is the price negotiable?",
                "time": "10:30 AM",
                "unread": "2"
            },
            {
                "name": "Green Valley Dairy",
                "message": "We will dispatch tomorrow",
                "time": "Yesterday",
                "unread": ""
            },
            {
                "name": "Ocean Catch Inc.",
                "message": "Contract accepted!",
                "time": "2 days ago",
                "unread": ""
            }
        ]

        y_offset = 200
        for chat in chats:
            # Chat item
            draw.rectangle([(50, y_offset), (1030, y_offset + 120)],
                          fill='#F9F9F9', outline='#E0E0E0', width=1)

            # Avatar (emoji)
            avatar = "👤"
            draw.text((70, y_offset + 15), avatar, fill='#2D5016', font=font_title)

            # Name
            draw.text((200, y_offset + 20), chat["name"], fill='#2D5016', font=font_text)

            # Message preview
            draw.text((200, y_offset + 60), chat["message"], fill='#666666', font=font_small)

            # Time
            draw.text((900, y_offset + 20), chat["time"], fill='#999999', font=font_small)

            # Unread badge
            if chat["unread"]:
                draw.ellipse([(950, y_offset + 50), (1020, y_offset + 100)],
                            fill='#FF5252', width=0)
                draw.text((975, y_offset + 60), chat["unread"], fill='white', font=font_small)

            y_offset += 140

        # Bottom navigation
        draw.rectangle([(0, HEIGHT - 120), (WIDTH, HEIGHT)], fill='#F5F5F5', width=0)
        nav_items = ["🏠 Home", "📋 Contracts", "💬 Chat", "⚙️ Settings"]
        x_start = 50
        for idx, item in enumerate(nav_items):
            color = '#2D5016' if idx == 2 else '#999999'
            draw.text((x_start, HEIGHT - 80), item, fill=color, font=font_small)
            x_start += 250

        return img

    def create_settings_screen():
        """Create settings screen"""
        img = Image.new('RGB', (WIDTH, HEIGHT), color='#FFFFFF')
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 50)
            font_text = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 28)
            font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 22)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Header
        draw.rectangle([(0, 0), (WIDTH, 150)], fill='#2D5016', width=0)
        draw.text((50, 50), "Settings", fill='white', font=font_title)

        # Profile section
        draw.text((50, 200), "👤 Profile", fill='#666666', font=font_small)

        settings = [
            ("Account Settings", "Manage your account"),
            ("Privacy & Security", "Control your data"),
            ("Notifications", "Manage alerts"),
            ("Payment Methods", "Add/edit payment"),
            ("About App", "Version 1.0.0"),
            ("Logout", "Sign out of account")
        ]

        y_offset = 300
        for setting, desc in settings:
            draw.rectangle([(50, y_offset), (1030, y_offset + 100)],
                          fill='#F9F9F9', outline='#E0E0E0', width=1)

            draw.text((70, y_offset + 15), setting, fill='#2D5016', font=font_text)
            draw.text((70, y_offset + 55), desc, fill='#999999', font=font_small)

            y_offset += 120

        # Bottom navigation
        draw.rectangle([(0, HEIGHT - 120), (WIDTH, HEIGHT)], fill='#F5F5F5', width=0)
        nav_items = ["🏠 Home", "📋 Contracts", "💬 Chat", "⚙️ Settings"]
        x_start = 50
        for idx, item in enumerate(nav_items):
            color = '#2D5016' if idx == 3 else '#999999'
            draw.text((x_start, HEIGHT - 80), item, fill=color, font=font_small)
            x_start += 250

        return img

    # Generate all screens
    screens = [
        ("splash", create_splash_screen()),
        ("login", create_login_screen()),
        ("dashboard", create_dashboard()),
        ("contracts", create_contracts_screen()),
        ("chat", create_chat_screen()),
        ("settings", create_settings_screen()),
    ]

    return screens

def main():
    """Main function to create and save Flutter app demo screens"""
    output_dir = "C:\\Users\\kodav\\Downloads\\Farming pdd"

    print("[*] Generating Flutter App UI Screens...")
    screens = create_flutter_app_screens()

    print(f"[*] Creating animated GIF from {len(screens)} screens...")

    # Create animated GIF
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    gif_path = os.path.join(output_dir, f"flutter_app_demo_{timestamp}.gif")

    images = [screen[1] for screen in screens]

    # Add some screens twice for better animation
    images = images + [images[-1]] * 10  # Pause on last screen

    images[0].save(
        gif_path,
        save_all=True,
        duration=1000,  # 1 second per frame
        loop=0,
        optimize=False
    )

    print(f"[+] Flutter app demo GIF created!")
    print(f"    File: {os.path.basename(gif_path)}")
    print(f"    Path: {gif_path}")
    print(f"    Size: {os.path.getsize(gif_path) / 1024:.2f} KB")
    print(f"    Duration: {len(images)} seconds")

    # Save individual screens as reference
    for name, img in screens:
        png_path = os.path.join(output_dir, f"flutter_screen_{name}.png")
        img.save(png_path)
        print(f"[*] Saved: flutter_screen_{name}.png")

    print("[+] Flutter app demo complete!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

