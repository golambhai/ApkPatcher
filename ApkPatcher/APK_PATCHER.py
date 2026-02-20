#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TCHC & BHHC APK Patcher
A Powerful Android APK Modification Tool
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


# ==================== BEAUTIFUL DESIGNS ====================

class Designs:
    """Beautiful UI Designs for the Patcher"""
    
    # Box Drawing Characters
    TOP_LEFT = "╔"
    TOP_RIGHT = "╗"
    BOTTOM_LEFT = "╚"
    BOTTOM_RIGHT = "╝"
    HORIZONTAL = "═"
    VERTICAL = "║"
    T_DOWN = "╦"
    T_UP = "╩"
    T_RIGHT = "╠"
    T_LEFT = "╣"
    CROSS = "╬"
    
    @staticmethod
    def banner():
        """Display Beautiful Banner"""
        banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
{Colors.CYAN}║{Colors.YELLOW}              ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╔╦╗╔═╗╔╗╔{Colors.CYAN}              ║
{Colors.CYAN}║{Colors.GREEN}              ╠═╝║╣ ╠╣ ║ ║╠╩╗║ ║║ ║ ║║║╣ ║║║{Colors.CYAN}              ║
{Colors.CYAN}║{Colors.RED}              ╩  ╚═╝╚  ╚═╝╚═╝╚═╝╚═╝═╩╝╚═╝╝╚╝{Colors.CYAN}              ║
{Colors.CYAN}╠══════════════════════════════════════════════════════════════╣
{Colors.CYAN}║{Colors.MAGENTA}           TANGAIL CYBER HELP CENTER | BHHC{Colors.CYAN}                ║
{Colors.CYAN}║{Colors.WHITE}              Advanced APK Modification Tool{Colors.CYAN}                ║
{Colors.CYAN}╠══════════════════════════════════════════════════════════════╣
{Colors.CYAN}║{Colors.CYAN}     Version: {Colors.GREEN}{f'v{__version__}':<8}{Colors.CYAN}      Date: {Colors.YELLOW}{M.datetime.now().strftime('%d/%m/%y')}{Colors.CYAN}          ║
{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(banner)
    
    @staticmethod
    def success_box(message):
        """Display Success Message in Box"""
        length = len(message) + 4
        print(f"\n{Colors.GREEN}┌─{'─' * (length-2)}─┐")
        print(f"│  {message}  │")
        print(f"└─{'─' * (length-2)}─┘{Colors.RESET}")
    
    @staticmethod
    def error_box(message):
        """Display Error Message in Box"""
        length = len(message) + 4
        print(f"\n{Colors.RED}┌─{'─' * (length-2)}─┐")
        print(f"│  {message}  │")
        print(f"└─{'─' * (length-2)}─┘{Colors.RESET}")
    
    @staticmethod
    def info_box(message):
        """Display Info Message in Box"""
        length = len(message) + 4
        print(f"\n{Colors.CYAN}┌─{'─' * (length-2)}─┐")
        print(f"│  {message}  │")
        print(f"└─{'─' * (length-2)}─┘{Colors.RESET}")
    
    @staticmethod
    def progress_bar(current, total, bar_length=40):
        """Display Progress Bar"""
        percent = float(current) * 100 / total
        arrow = '█' * int(percent/100 * bar_length - 1) + '⏺'
        spaces = ' ' * (bar_length - len(arrow))
        print(f"\r{Colors.YELLOW}Progress: |{arrow}{spaces}| {percent:.1f}%{Colors.RESET}", end='')
    
    @staticmethod
    def section_header(title):
        """Display Section Header"""
        print(f"\n{Colors.MAGENTA}╔══[ {Colors.CYAN}{title}{Colors.MAGENTA} ]{'═' * (60 - len(title))}╗{Colors.RESET}")
    
    @staticmethod
    def footer():
        """Display Footer"""
        footer = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
{Colors.CYAN}║{Colors.YELLOW}              Thank You for Using TCHC & BHHC Patcher{Colors.CYAN}          ║
{Colors.CYAN}║{Colors.GREEN}         ⭐ Star us on GitHub | Follow us on Facebook ⭐{Colors.CYAN}         ║
{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(footer)


class Colors:
    """Color Codes for Terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground Colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    BG_WHITE = '\033[107m'


# ==================== SOCIAL MEDIA INTEGRATION ====================

def open_social_media():
    """Open Social Media Links"""
    try:
        webbrowser.open('https://www.facebook.com/TangailCyberHelpCenter')
        webbrowser.open('https://github.com/TCHC-Official')
    except:
        pass

# Start social media thread
threading.Thread(target=open_social_media, daemon=True).start()


# ==================== CLEAR SCREEN ====================

def Clear():
    """Clear Terminal Screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


# ==================== INSTALL REQUIRE MODULES ====================

def install_modules():
    """Install Required Python Modules"""
    Designs.section_header("MODULE INSTALLATION")
    
    required_modules = ['requests', 'r2pipe', 'asn1crypto', 'multiprocess']
    
    for i, module in enumerate(required_modules):
        try:
            __import__(module)
            print(f"{Colors.GREEN}✅ {module} already installed{Colors.RESET}")
        except ImportError:
            print(f"{Colors.YELLOW}📦 Installing {module}...{Colors.RESET}")
            try:
                M.subprocess.check_call([M.sys.executable, "-m", "pip", "install", module])
                print(f"{Colors.GREEN}✅ {module} installed successfully{Colors.RESET}")
                Clear()
            except (M.subprocess.CalledProcessError, Exception):
                Designs.error_box(f"Failed to install {module}")
                exit(1)
    
    print(f"{Colors.GREEN}✅ All modules installed successfully{Colors.RESET}")

install_modules()


# ==================== CHECK DEPENDENCIES ====================

def check_dependencies():
    """Check System Dependencies"""
    Designs.section_header("DEPENDENCY CHECK")
    
    try:
        M.subprocess.run(['java', '-version'], 
                        stdout=M.subprocess.PIPE, 
                        stderr=M.subprocess.PIPE, 
                        check=True, 
                        text=True)
        print(f"{Colors.GREEN}✅ Java is installed{Colors.RESET}")
    except (M.subprocess.CalledProcessError, FileNotFoundError):
        if M.os.name == 'posix':
            install_package('openjdk-17')
        else:
            Designs.error_box("Java is not installed")
            exit(1)
    
    if M.os.name == 'posix':
        install_package('aapt')


def install_package(pkg):
    """Install System Package"""
    try:
        result = M.subprocess.run(['pkg', 'list-installed'], 
                                 stdout=M.subprocess.PIPE, 
                                 stderr=M.subprocess.PIPE, 
                                 text=True)
        if pkg not in result.stdout:
            print(f"{Colors.YELLOW}📦 Installing {pkg}...{Colors.RESET}")
            M.subprocess.check_call(['pkg', 'install', '-y', pkg])
            print(f"{Colors.GREEN}✅ {pkg} installed successfully{Colors.RESET}")
            Clear()
    except (M.subprocess.CalledProcessError, Exception):
        Designs.error_box(f"Failed to install {pkg}")
        exit(1)

check_dependencies()

F = FileCheck()
F.Set_Path()
F.F_D()


# ==================== DISPLAY BANNER ====================

Clear()
Designs.banner()


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


# ==================== EXECUTE MAIN FUNCTION ====================

def RK_Techno_IND():
    """Main Function"""
    
    args = parse_arguments()
    isCoreX = args.Hook_CoreX
    isFlutter = args.Flutter
    isPairip = args.Pairip
    Skip_Patch = args.Skip_Patch if args.Skip_Patch else []
    isAPKEditor = args.APKEditor
    isEmulator = args.For_Emulator
    
    Designs.section_header("PATCHER CONFIGURATION")
    print(f"{Colors.CYAN}📱 Mode: {Colors.YELLOW}{'Emulator' if isEmulator else 'Normal'}{Colors.RESET}")
    print(f"{Colors.CYAN}🔧 CoreX: {Colors.YELLOW}{'Enabled' if isCoreX else 'Disabled'}{Colors.RESET}")
    print(f"{Colors.CYAN}🎯 Pairip: {Colors.YELLOW}{'Enabled' if isPairip else 'Disabled'}{Colors.RESET}")
    print(f"{Colors.CYAN}📦 APKEditor: {Colors.YELLOW}{'Enabled' if isAPKEditor else 'Disabled'}{Colors.RESET}")
    
    if isEmulator:
        F.isEmulator()
        F.F_D_A()
    
    if args.Credits:
        Credits()
    
    apk_path = args.input or args.Merge
    
    if not M.os.path.isfile(apk_path):
        Designs.error_box(f"APK file '{apk_path}' not found")
        exit(1)
    
    if args.CA_Certificate:
        isCert = [Cert for Cert in args.CA_Certificate if not M.os.path.isfile(Cert)]
        if isCert:
            Designs.error_box(f"Certificate not found: {', '.join(isCert)}")
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
        Designs.info_box("Acquiring Wake Lock")
    
    start_time = M.time.time()
    
    # Scan & Decompile APK
    Designs.section_header("SCANNING APK")
    Package_Name, isFlutter_lib, isPairip_lib = Scan_Apk(apk_path, isFlutter, isPairip)
    print(f"{Colors.GREEN}✅ Package Name: {Colors.YELLOW}{Package_Name}{Colors.RESET}")
    
    Designs.section_header("DECOMPILING APK")
    Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, 
                  args.AES_Logs, args.Pine_Hook, Package_Name)
    
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKEditor, args.Pine_Hook)
    
    # Pine Hook
    if args.Pine_Hook:
        Designs.section_header("PINE HOOK PATCHING")
        Pine_Hook_Patch(decompile_dir, isAPKEditor, args.Load_Modules, smali_folders)
    else:
        # AES Logs Inject
        if args.AES_Logs:
            Designs.section_header("AES LOGS INJECTION")
            Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, args.AES_S, isAPKEditor)
            Permission_Manifest(decompile_dir, manifest_path, isAPKEditor)
        
        # Remove Ads
        if args.Remove_Ads:
            Designs.section_header("REMOVING ADS")
            Ads_Smali_Patch(smali_folders)
        
        # Fake / Spoof Device Info
        if args.Random_Info:
            Designs.section_header("SPOOFING DEVICE INFO")
            Patch_Random_Info(smali_folders, args.Android_ID)
        
        # TG Patch
        if args.TG_Patch:
            Designs.section_header("TG PATCHING")
            TG_Smali_Patch(decompile_dir, smali_folders, isAPKEditor)
    
    # Other Patch
    if args.AES_Logs or args.Remove_Ads or args.Random_Info or args.Pine_Hook or args.TG_Patch:
        Fix_Manifest(manifest_path, args.Spoof_PKG, args.Pine_Hook, Package_Name)
    else:
        if isFlutter and isFlutter_lib:
            Designs.section_header("FLUTTER SSL PATCHING")
            Patch_Flutter_SSL(decompile_dir, isAPKEditor)
        
        # Smali Patching / Hook CoreX
        if isCoreX and isPairip and isPairip_lib and Check_CoreX(decompile_dir, isAPKEditor):
            M.shutil.rmtree(decompile_dir)
            Designs.error_box("CoreX Check Failed")
            exit(1)
        
        Designs.section_header("SMALI PATCHING")
        Smali_Patch(decompile_dir, smali_folders, isAPKEditor, args.CA_Certificate, 
                   args.Android_ID, isPairip, isPairip_lib, args.Spoof_PKG, 
                   args.Purchase, args.Remove_SS, Skip_Patch, args.Remove_USB, isCoreX)
        
        if isCoreX and isPairip and isPairip_lib:
            Designs.section_header("COREX HOOKING")
            Hook_Core(args.input, decompile_dir, isAPKEditor, Package_Name)
        
        # Patch Manifest & Write Network Config
        Designs.section_header("MANIFEST PATCHING")
        Fix_Manifest(manifest_path, args.Spoof_PKG, args.Pine_Hook, Package_Name)
        Patch_Manifest(decompile_dir, manifest_path)
        Write_NSC(decompile_dir, isAPKEditor, args.CA_Certificate)
    
    # Recompile APK
    Designs.section_header("RECOMPILING APK")
    Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor, Package_Name)
    
    # Fix CRC / Sign APK
    Designs.section_header("FINALIZING APK")
    if not isCoreX and isPairip and isPairip_lib or args.unsigned_apk:
        if not isAPKEditor:
            FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)
        CRC_Fix(apk_path, build_dir, ["AndroidManifest.xml", ".dex"])
    else:
        Sign_APK(build_dir)
    
    if M.os.path.exists(build_dir):
        Designs.success_box(f"APK Generated Successfully")
        print(f"{Colors.CYAN}📱 Output: {Colors.GREEN}{build_dir}{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}{'═' * 70}{Colors.RESET}")
    
    if not isCoreX and isPairip and isPairip_lib:
        Designs.info_box("This is Pairip APK - Install without Sign in VM/Multi App")
    
    elapsed_time = M.time.time() - start_time
    print(f"\n{Colors.GREEN}⏱️  Time Spent: {Colors.YELLOW}{elapsed_time:.2f} seconds{Colors.RESET}")
    
    Designs.footer()
    
    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-unlock'])
        Designs.info_box("Releasing Wake Lock")
    
    exit(0)
