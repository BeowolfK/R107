#!/usr/bin/env python3
"""Exercice 2 (Partie 4) du TP6"""

def get_login(uid, liste):
    """Renvoie le login correspondant a l'uid passé en parametre dans la liste d'utilisateurs"""
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == int(info[2]):
            return info[0]

def get_name(uid, liste):
    """Renvoie le nom correspondant a l'uid passé en parametre dans la liste d'utilisateurs"""
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == int(info[2]):
            return info[4].split(',')[0]

def get_home(uid, liste):
    """Renvoie le home correspondant a l'uid passé en parametre dans la liste d'utilisateurs"""
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == int(info[2]):
            return info[5]

def get_shell(uid, liste):
    """Renvoie le shell correspondant a l'uid passé en parametre dans la liste d'utilisateurs"""
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == int(info[2]):
            return info[6]
            
def get_gid(uid, liste):
    """Renvoie le gid correspondant a l'uid passé en parametre dans la liste d'utilisateurs"""
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == int(info[2]):
            return info[3]

def get_group_members(gid, groups):
    """Renvoie la liste des logins correspondant au gid passé en parametre dans la liste de groups"""
    assert isinstance(gid, int)
    assert isinstance(groups, list) 
    for group in groups:
        info = group.split(':')
        if gid == int(info[2]):
            if info[3] == '':
                return []
            return info[3].split(',')

def get_user_groups(uid, users, groups):
    """Renvoie la liste des identifiants des groupes auquel appartient l'utilisateur ayant pour identifiant uid"""
    assert isinstance(uid, int)
    assert isinstance(users, list)
    assert isinstance(groups, list)
    username = get_login(uid, users)
    nbr = [int(get_gid(uid, users))]
    for group in groups:
        info = group.split(':')
        gid = info[2]
        user_group = info[-1].split(',')
        if username in user_group:
            nbr.append(int(gid))
    return nbr



def main():
    utilisateurs = [
        "usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin",
        "dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin",
        "rtkit:x:109:114:RealtimeKit,,,:/proc:/usr/sbin/nologin",
        "lightdm:x:110:115:Light Display Manager:/var/lib/lightdm:/bin/false",
        "cups-pk-helper:x:111:118:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin",
        "speech-dispatcher:x:112:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false",
        "whoopsie:x:113:119::/nonexistent:/bin/false",
        "kernoops:x:114:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin",
        "saned:x:115:121::/var/lib/saned:/usr/sbin/nologin",
        "pulse:x:116:122:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin",
        "avahi:x:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin",
        "colord:x:118:125:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin",
        "hplip:x:119:7:HPLIP system user,,,:/var/run/hplip:/bin/false",
        "wurbel:x:1000:1000:Éric Würbel,,,:/home/wurbel:/bin/bash",
    ]

    groupes = [
        "adm:x:4:syslog,wurbel",
        "tty:x:5:wurbel",
        "disk:x:6:",
        "lp:x:7:",
        "mail:x:8:",
        "news:x:9:",
        "uucp:x:10:wurbel",
        "man:x:12:",
        "proxy:x:13:",
        "kmem:x:15:",
        "dialout:x:20:wurbel",
        "fax:x:21:",
        "voice:x:22:",
        "cdrom:x:24:wurbel",
        "floppy:x:25:",
        "tape:x:26:",
        "sudo:x:27:wurbel",
        "audio:x:29:pulse,wurbel",
    ]

    assert get_login(1000, utilisateurs) == "wurbel"
    assert get_login(109, utilisateurs) == "rtkit"
    assert get_login(111, utilisateurs) == "cups-pk-helper"
    assert get_login(1125, utilisateurs) is None
    print("Tous les tests sur les logins sont passés")

    assert get_name(1000, utilisateurs) == "Éric Würbel"
    assert get_name(109, utilisateurs) == "RealtimeKit"
    assert get_name(111, utilisateurs) == "user for cups-pk-helper service"
    assert get_name(1125, utilisateurs) is None
    print("Tous les tests sur les noms sont passés")

    assert get_home(1000, utilisateurs) == "/home/wurbel"
    assert get_home(109, utilisateurs) == "/proc"
    assert get_home(111, utilisateurs) == "/home/cups-pk-helper"
    assert get_home(1125, utilisateurs) is None
    print("Tous les tests sur les home sont passés")

    assert get_shell(1000, utilisateurs) == "/bin/bash"
    assert get_shell(109, utilisateurs) == "/usr/sbin/nologin"
    assert get_shell(111, utilisateurs) == "/usr/sbin/nologin"
    assert get_shell(1125, utilisateurs) is None
    print("Tous les tests sur les shell sont passés")

    assert get_group_members(4, groupes) == ['syslog', 'wurbel']
    assert get_group_members(13, groupes) ==  []
    assert get_group_members(27, groupes) ==  ['wurbel']
    assert get_group_members(1300, groupes) is None
    print("Tous les tests sur les membres des groupes sont passés")

    assert get_user_groups(1000, utilisateurs, groupes) == [1000, 4, 5, 10, 20, 24, 27, 29]
    assert get_user_groups(116, utilisateurs, groupes) == [122, 29]
    assert get_user_groups(116, utilisateurs, groupes) == [122, 29]
    print("Tout les test sur les gid selon l'uid sont passés")
    
if __name__ == '__main__':
    main()