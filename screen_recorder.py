#!/usr/bin/env python3
"""
Screen Recording Script - Records the screen for app demo
"""

import subprocess
import time
import threading
from datetime import datetime
import sys

def record_screen_with_powershell(output_path, duration=60):
    """Record screen using PowerShell and FFmpeg via pipe"""
    print(f"[*] Attempting to record screen for {duration} seconds...")
    print(f"[*] Output: {output_path}")

    try:
        # Try to install required packages
        subprocess.run([sys.executable, "-m", "pip", "install", "pillow", "mss"],
                      capture_output=True, timeout=30)

        # Use mss for screen capture
        import mss
        from PIL import Image
        import io

        frames = []
        start_time = time.time()
        fps = 2  # 2 frames per second

        print(f"[*] Starting screen capture...")

        with mss.mss() as sct:
            while time.time() - start_time < duration:
                try:
                    # Capture primary monitor
                    screenshot = sct.grab(sct.monitors[1])
                    frame = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
                    frames.append(frame)

                    elapsed = int(time.time() - start_time)
                    print(f"[*] Recording... {elapsed}/{duration}s", end='\r')

                    time.sleep(1/fps)  # Maintain FPS
                except Exception as e:
                    print(f"[!] Error capturing frame: {e}")
                    continue

        print(f"\n[*] Captured {len(frames)} frames")

        if frames:
            print(f"[*] Saving video as GIF...")
            frames[0].save(
                output_path,
                save_all=True,
                duration=500//fps,  # 500ms per frame at 2fps
                loop=0,
                optimize=False
            )
            print(f"[+] Video saved successfully!")
            return True
        else:
            print(f"[!] No frames captured")
            return False

    except Exception as e:
        print(f"[!] Error: {e}")
        return False

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"C:\\Users\\kodav\\Downloads\\Farming pdd\\app_demo_{timestamp}.gif"

    success = record_screen_with_powershell(output_file, duration=45)

    if success:
        print(f"\n[+] Recording complete: {output_file}")
        sys.exit(0)
    else:
        print(f"\n[!] Recording failed")
        sys.exit(1)

