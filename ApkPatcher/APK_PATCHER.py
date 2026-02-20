#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TCHC & BANGLADESH HACKING HELP CENTRE
Professional Android APK Modification Tool
Developer: ZX ROCK 007
"""

from .CLI import parse_arguments
from .ANSI_COLORS import ANSI
C = ANSI()
from .MODULES import IMPORT
M = IMPORT()

from ApkPatcher.Utils.CRC import CRC_Fix
from ApkPatcher.Utils.Credits import Credits
from ApkPatcher.Utils.Scan import Scan_Apk
from ApkPatcher.Utils.Anti_Splits import Anti_Split
from ApkPatcher.Utils.Files_Check import FileCheck, __version__
from ApkPatcher.Utils.Decompile_Compile import Decompile_Apk, Recompile_Apk, FixSigBlock, Sign_APK

from ApkPatcher.Patch.AES import Copy_AES_Smali
from ApkPatcher.Patch.CERT_NSC import Write_NSC
from ApkPatcher.Patch.Smali_Patch import Smali_Patch
from ApkPatcher.Patch.TG_Patch import TG_Smali_Patch
from ApkPatcher.Patch.Ads_Patch import Ads_Smali_Patch
from ApkPatcher.Patch.Pine_Hook import Pine_Hook_Patch
from ApkPatcher.Patch.Spoof_Patch import Patch_Random_Info
from ApkPatcher.Patch.Flutter_SSL_Patch import Patch_Flutter_SSL
from ApkPatcher.Patch.Pairip_CoreX import Check_CoreX, Hook_Core
from ApkPatcher.Patch.Manifest_Patch import Fix_Manifest, Patch_Manifest, Permission_Manifest

import webbrowser
import threading
import os
import sys
import time


# ==================== COLOR SYSTEM ====================

class Colors:
    """Extended Color System - Must be defined before use"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'
    
    # Foreground Colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bright Foreground Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    BG_WHITE = '\033[107m'


# ==================== ADVANCED UI DESIGNS ====================

class UltimateDesign:
    """Professional UI Design System"""
    
    # Box Drawing Characters (Double Line)
    TL = "╔"
    TR = "╗"
    BL = "╚"
    BR = "╝"
    H = "═"
    V = "║"
    TD = "╦"
    TU = "╩"
    TRIGHT = "╠"
    TLEFT = "╣"
    CROSS = "╬"
    
    # Single Line Characters
    S_TL = "┌"
    S_TR = "┐"
    S_BL = "└"
    S_BR = "┘"
    S_H = "─"
    S_V = "│"
    
    @staticmethod
def cyber_banner():
    """Display Cyber Themed Banner with TCHC"""
    current_date = time.strftime('%d/%m/%y')
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
{Colors.CYAN}║{Colors.RED}  ████████╗ ██████╗██╗  ██╗ ██████╗ {Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}║{Colors.RED}  ╚══██╔══╝██╔════╝██║  ██║██╔════╝ {Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}║{Colors.RED}     ██║   ██║     ███████║██║      {Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}║{Colors.RED}     ██║   ██║     ██╔══██║██║      {Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}║{Colors.RED}     ██║   ╚██████╗██║  ██║╚██████╔╝{Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}║{Colors.RED}     ╚═╝    ╚═════╝╚═╝  ╚═╝ ╚═════╝ {Colors.RESET}                                  {Colors.CYAN}║
{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣
{Colors.CYAN}║{Colors.YELLOW}                  ████████╗ █████╗ ████╗  ██╗ ██████╗  █████╗ ██╗██╗     {Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                  ╚══██╔══╝██╔══██╗██╔██╗ ██║██╔════╝ ██╔══██╗██║██║     {Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                     ██║   ███████║██║╚██╗██║██║  ███╗███████║██║██║     {Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                     ██║   ██╔══██║██║ ╚████║██║   ██║██╔══██║██║██║     {Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                     ██║   ██║  ██║██║  ╚███║╚██████╔╝██║  ██║██║███████╗{Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                     ╚═╝   ╚═╝  ╚═╝╚═╝   ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝{Colors.CYAN}║
{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣
{Colors.CYAN}║{Colors.MAGENTA}           ╔═══════════════════════════════════════════════════════╗           {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}           ║  {Colors.CYAN}TANGAIL CYBER HELP CENTER{Colors.MAGENTA}  |  {Colors.GREEN}BANGLADESH HACKING HELP CENTRE  {Colors.MAGENTA}║           {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}           ╚═══════════════════════════════════════════════════════╝           {Colors.CYAN}║
{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣
{Colors.CYAN}║{Colors.WHITE}                         ╔════════════════════════════════════╗                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ║                                    ║                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ║     {Colors.RED}OWNER: ZX ROCK 007{Colors.WHITE}            ║                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ║     {Colors.YELLOW}VERSION: v{__version__}{Colors.WHITE}               ║                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ║     {Colors.GREEN}DATE: {current_date}{Colors.WHITE}                ║                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ║                                    ║                         {Colors.CYAN}║
{Colors.CYAN}║{Colors.WHITE}                         ╚════════════════════════════════════╝                         {Colors.CYAN}║
{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)
    
    @staticmethod
    def matrix_effect(text, delay=0.05):
        """Display text with matrix-like effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def loading_animation(message, duration=2):
        """Display loading animation"""
        animation = "|/-\\"
        for i in range(duration * 10):
            sys.stdout.write(f"\r{Colors.CYAN}{message} {animation[i % 4]}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
    
    @staticmethod
    def progress_bar(current, total, prefix='Progress', suffix='Complete', length=50):
        """Display a beautiful progress bar"""
        percent = (current / total) * 100
        filled_length = int(length * current // total)
        bar = '█' * filled_length + '░' * (length - filled_length)
        
        # Color gradient effect
        if percent < 30:
            color = Colors.RED
        elif percent < 70:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
            
        print(f'\r{color}{prefix}: |{bar}| {percent:.1f}% {suffix}{Colors.RESET}', end='\r')
        if current == total:
            print()
    
    @staticmethod
    def section_divider(title, char="═", color=Colors.CYAN):
        """Create a beautiful section divider"""
        width = 80
        side_width = (width - len(title) - 2) // 2
        print(f"\n{color}{char * side_width} [ {Colors.YELLOW}{title}{color} ] {char * side_width}{Colors.RESET}")
    
    @staticmethod
    def success_box(message):
        """Display success message in a box"""
        print(f"\n{Colors.GREEN}┌─{Colors.BRIGHT_GREEN}✓{Colors.GREEN}─{Colors.GREEN}{'─' * (len(message))}─┐")
        print(f"│  {Colors.WHITE}{message}{Colors.GREEN}  │")
        print(f"└─{'─' * (len(message) + 4)}─┘{Colors.RESET}")
    
    @staticmethod
    def error_box(message):
        """Display error message in a box"""
        print(f"\n{Colors.RED}┌─{Colors.BRIGHT_RED}✗{Colors.RED}─{Colors.RED}{'─' * (len(message))}─┐")
        print(f"│  {Colors.WHITE}{message}{Colors.RED}  │")
        print(f"└─{'─' * (len(message) + 4)}─┘{Colors.RESET}")
    
    @staticmethod
    def info_box(message):
        """Display info message in a box"""
        print(f"\n{Colors.CYAN}┌─{Colors.BRIGHT_CYAN}ℹ{Colors.CYAN}─{Colors.CYAN}{'─' * (len(message))}─┐")
        print(f"│  {Colors.WHITE}{message}{Colors.CYAN}  │")
        print(f"└─{'─' * (len(message) + 4)}─┘{Colors.RESET}")
    
    @staticmethod
    def warning_box(message):
        """Display warning message in a box"""
        print(f"\n{Colors.YELLOW}┌─{Colors.BRIGHT_YELLOW}⚠{Colors.YELLOW}─{Colors.YELLOW}{'─' * (len(message))}─┐")
        print(f"│  {Colors.WHITE}{message}{Colors.YELLOW}  │")
        print(f"└─{'─' * (len(message) + 4)}─┘{Colors.RESET}")
    
    @staticmethod
    def table_view(data, headers):
        """Display data in a formatted table"""
        col_widths = [len(h) for h in headers]
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Create table border
        def create_border(joiner):
            return joiner.join(['─' * (w + 2) for w in col_widths])
        
        print(f"\n{Colors.CYAN}┌{create_border('┬')}┐")
        
        # Headers
        header_row = "│"
        for i, header in enumerate(headers):
            header_row += f" {Colors.YELLOW}{header:<{col_widths[i]}}{Colors.CYAN} │"
        print(header_row)
        
        print(f"├{create_border('┼')}┤")
        
        # Data rows
        for row in data:
            data_row = f"{Colors.CYAN}│"
            for i, cell in enumerate(row):
                data_row += f" {Colors.WHITE}{str(cell):<{col_widths[i]}}{Colors.CYAN} │"
            print(data_row)
        
        print(f"└{create_border('┴')}┘{Colors.RESET}")
    
    @staticmethod
    def animated_logo():
        """Display animated TCHC logo"""
        logo_frames = [
            f"""{Colors.RED}    ╔╗ ╔╗ ╔══╗ ╔══╗ ╔╗╔╗{Colors.RESET}""",
            f"""{Colors.YELLOW}    ║║ ║║ ║══╣ ║══╣ ║╚╝║{Colors.RESET}""",
            f"""{Colors.GREEN}    ║╚═╝║ ╠══║ ╠══║ ║╔╗║{Colors.RESET}""",
            f"""{Colors.CYAN}    ╚═══╝ ╚══╝ ╚══╝ ╚╝╚╝{Colors.RESET}"""
        ]
        
        for _ in range(3):  # Animate 3 times
            for frame in logo_frames:
                sys.stdout.write('\r' + frame)
                sys.stdout.flush()
                time.sleep(0.1)
        print()
    
    @staticmethod
    def footer():
        """Display professional footer"""
        footer = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
{Colors.CYAN}║{Colors.GREEN}          Thank you for using TCHC & Bangladesh Hacking Help Centre         {Colors.CYAN}║
{Colors.CYAN}║{Colors.YELLOW}                     Developer: {Colors.RED}ZX ROCK 007{Colors.YELLOW} | Version: v{__version__}                     {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}              ╔═══════════════════════════════════════════╗               {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}              ║  {Colors.CYAN}🔵 Facebook: Tangail Cyber Help Center{Colors.MAGENTA}      ║               {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}              ║  {Colors.GREEN}💚 GitHub: TCHC-Official{Colors.MAGENTA}                    ║               {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}              ║  {Colors.YELLOW}⭐ Star us on GitHub | Follow us on Facebook ⭐{Colors.MAGENTA}  ║               {Colors.CYAN}║
{Colors.CYAN}║{Colors.MAGENTA}              ╚═══════════════════════════════════════════╝               {Colors.CYAN}║
{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(footer)


# ==================== SOCIAL MEDIA INTEGRATION ====================

def open_social_media():
    """Open Social Media Links"""
    try:
        webbrowser.open('https://www.facebook.com/TangailCyberHelpCenter')
        webbrowser.open('https://github.com/TCHC-Official')
        webbrowser.open('https://www.facebook.com/BangladeshHackingHelpCentre')
    except:
        pass

# Start social media thread
threading.Thread(target=open_social_media, daemon=True).start()


# ==================== CLEAR SCREEN ====================

def Clear():
    """Clear Terminal Screen with Animation"""
    if os.name == 'nt':
        os.system('cls')
    else:
        print(f"{Colors.GREEN}Clearing screen{Colors.RESET}", end='')
        for i in range(3):
            time.sleep(0.3)
            print(".", end='', flush=True)
        time.sleep(0.3)
        os.system('clear')


# ==================== INSTALL REQUIRE MODULES ====================

def install_modules():
    """Install Required Python Modules with UI"""
    UltimateDesign.section_divider("MODULE INSTALLATION")
    
    required_modules = ['requests', 'r2pipe', 'asn1crypto', 'multiprocess']
    total_modules = len(required_modules)
    
    for i, module in enumerate(required_modules, 1):
        try:
            __import__(module)
            UltimateDesign.progress_bar(i, total_modules, "Checking Modules")
            print(f"{Colors.GREEN}  ✅ {module} already installed{Colors.RESET}")
        except ImportError:
            UltimateDesign.progress_bar(i, total_modules, "Installing Modules")
            print(f"{Colors.YELLOW}  📦 Installing {module}...{Colors.RESET}")
            try:
                M.subprocess.check_call([M.sys.executable, "-m", "pip", "install", module])
                print(f"{Colors.GREEN}  ✅ {module} installed successfully{Colors.RESET}")
                Clear()
            except (M.subprocess.CalledProcessError, Exception):
                UltimateDesign.error_box(f"Failed to install {module}")
                exit(1)
    
    UltimateDesign.success_box("All modules installed successfully")


# ==================== CHECK DEPENDENCIES ====================

def check_dependencies():
    """Check System Dependencies"""
    UltimateDesign.section_divider("DEPENDENCY CHECK")
    
    # Check Java
    try:
        M.subprocess.run(['java', '-version'], 
                        stdout=M.subprocess.PIPE, 
                        stderr=M.subprocess.PIPE, 
                        check=True, 
                        text=True)
        print(f"{Colors.GREEN}  ✅ Java is installed{Colors.RESET}")
    except (M.subprocess.CalledProcessError, FileNotFoundError):
        if M.os.name == 'posix':
            install_package('openjdk-17')
        else:
            UltimateDesign.error_box("Java is not installed")
            exit(1)
    
    # Check AAPT for Termux
    if M.os.name == 'posix':
        try:
            M.subprocess.run(['aapt', 'version'], 
                            stdout=M.subprocess.PIPE, 
                            stderr=M.subprocess.PIPE, 
                            check=True)
            print(f"{Colors.GREEN}  ✅ AAPT is installed{Colors.RESET}")
        except:
            install_package('aapt')
    
    UltimateDesign.success_box("All dependencies satisfied")


def install_package(pkg):
    """Install System Package"""
    try:
        result = M.subprocess.run(['pkg', 'list-installed'], 
                                 stdout=M.subprocess.PIPE, 
                                 stderr=M.subprocess.PIPE, 
                                 text=True)
        if pkg not in result.stdout:
            print(f"{Colors.YELLOW}  📦 Installing {pkg}...{Colors.RESET}")
            M.subprocess.check_call(['pkg', 'install', '-y', pkg])
            print(f"{Colors.GREEN}  ✅ {pkg} installed successfully{Colors.RESET}")
            Clear()
    except (M.subprocess.CalledProcessError, Exception):
        UltimateDesign.error_box(f"Failed to install {pkg}")
        exit(1)


# ==================== INITIALIZATION ====================

F = FileCheck()
F.Set_Path()
F.F_D()


# ==================== TARGET ALL CLASSES FOLDER ====================

def Find_Smali_Folders(decompile_dir, isAPKEditor, isPine_Hook):
    """Find Smali Folders in Decompiled Directory"""
    
    dex_path = M.os.path.join(decompile_dir, "dex") if isAPKEditor else decompile_dir
    smali_path = M.os.path.join(decompile_dir, "smali") if isAPKEditor else decompile_dir
    
    if isPine_Hook:
        classes_files = [file for file in M.os.listdir(dex_path) 
                        if file.startswith("classes") and file.endswith(".dex")]
        return f"classes{len(classes_files) + 1}.dex"
    else:
        prefix = "classes" if isAPKEditor else "smali_classes"
        folders = sorted([folder for folder in M.os.listdir(smali_path) 
                         if folder == "smali" or folder.startswith(prefix)], 
                        key=lambda x: int(x.split(prefix)[-1]) 
                        if x.split(prefix)[-1].isdigit() else 0)
        return [M.os.path.join(smali_path, folder) for folder in folders]


# ==================== MAIN EXECUTION ====================

def RK_Techno_IND():
    """Main Function with Professional UI"""
    
    Clear()
    UltimateDesign.cyber_banner()
    UltimateDesign.loading_animation("Initializing TCHC Patcher")
    
    args = parse_arguments()
    isCoreX = args.Hook_CoreX
    isFlutter = args.Flutter
    isPairip = args.Pairip
    Skip_Patch = args.Skip_Patch if args.Skip_Patch else []
    isAPKEditor = args.APKEditor
    isEmulator = args.For_Emulator
    
    # Display Configuration
    UltimateDesign.section_divider("PATCHER CONFIGURATION")
    
    config_data = [
        ["Mode", "Emulator" if isEmulator else "Normal"],
        ["CoreX", "✅ Enabled" if isCoreX else "❌ Disabled"],
        ["Pairip", "✅ Enabled" if isPairip else "❌ Disabled"],
        ["APKEditor", "✅ Enabled" if isAPKEditor else "❌ Disabled"],
        ["Flutter", "✅ Enabled" if isFlutter else "❌ Disabled"]
    ]
    UltimateDesign.table_view(config_data, ["Setting", "Value"])
    
    if isEmulator:
        F.isEmulator()
        F.F_D_A()
    
    if args.Credits:
        Credits()
    
    apk_path = args.input or args.Merge
    
    if not M.os.path.isfile(apk_path):
        UltimateDesign.error_box(f"APK file '{apk_path}' not found")
        exit(1)
    
    if args.CA_Certificate:
        isCert = [Cert for Cert in args.CA_Certificate if not M.os.path.isfile(Cert)]
        if isCert:
            UltimateDesign.error_box(f"Certificate not found: {', '.join(isCert)}")
            exit(1)
    
    apk_path = Anti_Split(apk_path, args.Merge, isCoreX)
    
    # Set All Paths Directory
    decompile_dir = M.os.path.join(M.os.path.expanduser("~"), 
                                   f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_decompiled")
    build_dir = M.os.path.abspath(M.os.path.join(M.os.path.dirname(apk_path), 
                                  f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_Patched.apk"))
    rebuild_dir = build_dir.replace('_Patched.apk', '_Patch.apk')
    manifest_path = M.os.path.join(decompile_dir, 'AndroidManifest.xml')
    
    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-lock'])
        UltimateDesign.info_box("Acquiring Wake Lock")
    
    start_time = M.time.time()
    
    # Scan & Decompile APK
    UltimateDesign.section_divider("SCANNING APK")
    UltimateDesign.loading_animation("Analyzing APK structure")
    Package_Name, isFlutter_lib, isPairip_lib = Scan_Apk(apk_path, isFlutter, isPairip)
    UltimateDesign.success_box(f"Package Name: {Package_Name}")
    
    UltimateDesign.section_divider("DECOMPILING APK")
    Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, 
                  args.AES_Logs, args.Pine_Hook, Package_Name)
    
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKEditor, args.Pine_Hook)
    
    # Pine Hook
    if args.Pine_Hook:
        UltimateDesign.section_divider("PINE HOOK PATCHING")
        Pine_Hook_Patch(decompile_dir, isAPKEditor, args.Load_Modules, smali_folders)
    else:
        # AES Logs Inject
        if args.AES_Logs:
            UltimateDesign.section_divider("AES LOGS INJECTION")
            Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, args.AES_S, isAPKEditor)
            Permission_Manifest(decompile_dir, manifest_path, isAPKEditor)
        
        # Remove Ads
        if args.Remove_Ads:
            UltimateDesign.section_divider("REMOVING ADS")
            Ads_Smali_Patch(smali_folders)
        
        # Fake / Spoof Device Info
        if args.Random_Info:
            UltimateDesign.section_divider("SPOOFING DEVICE INFO")
            Patch_Random_Info(smali_folders, args.Android_ID)
        
        # TG Patch
        if args.TG_Patch:
            UltimateDesign.section_divider("TG PATCHING")
            TG_Smali_Patch(decompile_dir, smali_folders, isAPKEditor)
    
    # Other Patch
    if args.AES_Logs or args.Remove_Ads or args.Random_Info or args.Pine_Hook or args.TG_Patch:
        Fix_Manifest(manifest_path, args.Spoof_PKG, args.Pine_Hook, Package_Name)
    else:
        if isFlutter and isFlutter_lib:
            UltimateDesign.section_divider("FLUTTER SSL PATCHING")
            Patch_Flutter_SSL(decompile_dir, isAPKEditor)
        
        # Smali Patching / Hook CoreX
        if isCoreX and isPairip and isPairip_lib and Check_CoreX(decompile_dir, isAPKEditor):
            M.shutil.rmtree(decompile_dir)
            UltimateDesign.error_box("CoreX Check Failed")
            exit(1)
        
        UltimateDesign.section_divider("SMALI PATCHING")
        Smali_Patch(decompile_dir, smali_folders, isAPKEditor, args.CA_Certificate, 
                   args.Android_ID, isPairip, isPairip_lib, args.Spoof_PKG, 
                   args.Purchase, args.Remove_SS, Skip_Patch, args.Remove_USB, isCoreX)
        
        if isCoreX and isPairip and isPairip_lib:
            UltimateDesign.section_divider("COREX HOOKING")
            Hook_Core(args.input, decompile_dir, isAPKEditor, Package_Name)
        
        # Patch Manifest & Write Network Config
        UltimateDesign.section_divider("MANIFEST PATCHING")
        Fix_Manifest(manifest_path, args.Spoof_PKG, args.Pine_Hook, Package_Name)
        Patch_Manifest(decompile_dir, manifest_path)
        Write_NSC(decompile_dir, isAPKEditor, args.CA_Certificate)
    
    # Recompile APK
    UltimateDesign.section_divider("RECOMPILING APK")
    Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor, Package_Name)
    
    # Fix CRC / Sign APK
    UltimateDesign.section_divider("FINALIZING APK")
    if not isCoreX and isPairip and isPairip_lib or args.unsigned_apk:
        if not isAPKEditor:
            FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)
        CRC_Fix(apk_path, build_dir, ["AndroidManifest.xml", ".dex"])
    else:
        Sign_APK(build_dir)
    
    # Final Output
    if M.os.path.exists(build_dir):
        UltimateDesign.success_box("APK Generated Successfully")
        print(f"{Colors.CYAN}  📱 Output: {Colors.GREEN}{build_dir}{Colors.RESET}")
    
    elapsed_time = M.time.time() - start_time
    UltimateDesign.info_box(f"Total Time: {elapsed_time:.2f} seconds")
    
    UltimateDesign.footer()
    
    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-unlock'])
        UltimateDesign.info_box("Releasing Wake Lock")
    
    exit(0)


# ==================== MAIN GUARD ====================

if __name__ == "__main__":
    try:
        install_modules()
        check_dependencies()
        RK_Techno_IND()
    except KeyboardInterrupt:
        UltimateDesign.warning_box("Process interrupted by user")
        sys.exit(0)
    except Exception as e:
        UltimateDesign.error_box(f"An error occurred: {str(e)}")
        sys.exit(1)
