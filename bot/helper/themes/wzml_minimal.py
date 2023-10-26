#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://www.github.com/BalaPriyanB/Copy-Master'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/TomenBots'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own TomenBots Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b><i>BOT STATISTICS :</i></b>
↦ <b>Bot Uptime :</b> {bot_uptime}

↦ <b><i>RAM ( MEMORY ) :</i></b>
↦ {ram_bar} {ram}%
↦ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

↦ <b><i>SWAP MEMORY :</i></b>
↦ {swap_bar} {swap}%
↦ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

↦ <b><i>DISK :</i></b>
↦ {disk_bar} {disk}%
↦ <b>Total Disk Read :</b> {disk_read}
↦ <b>Total Disk Write :</b> {disk_write}
↦ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
↦ <b>OS Uptime :</b> {os_uptime}
↦ <b>OS Version :</b> {os_version}
↦ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
↦ <b>Upload Data:</b> {up_data}
↦ <b>Download Data:</b> {dl_data}
↦ <b>Pkts Sent:</b> {pkt_sent}k
↦ <b>Pkts Received:</b> {pkt_recv}k
↦ <b>Total I/O Data:</b> {tl_data}

↦ <b>CPU :</b>
↦ {cpu_bar} {cpu}%
↦ <b>CPU Frequency :</b> {cpu_freq}
↦ <b>System Avg Load :</b> {sys_load}
↦ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
↦ <b>Total Core(s) :</b> {total_core}
↦ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>REPO STATISTICS :</i></b>
↦ <b>Bot Updated :</b> {last_commit}
↦ <b>Current Version :</b> {bot_version}
↦ <b>Latest Version :</b> {lat_version}
↦ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>BOT LIMITATIONS :</i></b>
↦ <b>Direct Limit :</b> {DL} GB
↦ <b>Torrent Limit :</b> {TL} GB
↦ <b>GDrive Limit :</b> {GL} GB
↦ <b>YT-DLP Limit :</b> {YL} GB
↦ <b>Playlist Limit :</b> {PL}
↦ <b>Mega Limit :</b> {ML} GB
↦ <b>Clone Limit :</b> {CL} GB
↦ <b>Leech Limit :</b> {LL} GB

↦ <b>Token Validity :</b> {TV}
↦ <b>User Time Limit :</b> {UTI} / task
↦ <b>User Parallel Tasks :</b> {UT}
↦ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
↦ <b>Date:</b> {date}
↦ <b>Time:</b> {time}
↦ <b>TimeZone:</b> {timz}
↦ <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
↦ <b>Mode:</b> {Mode}
↦ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
↦ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "⇢ <b><u>Task Started :</u></b>\n┃\n↦ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "⇢ <b><u>Leech Started :</u></b>\n┃\n↦ <b>User :</b> {mention} ( #ID{uid} )\n↦ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '↦ <b>Size: </b>{Size}\n'
    ELAPSE =                '↦ <b>Elapsed: </b>{Time}\n'
    MODE =                  '↦ <b>Mode: </b>{Mode}\n'
    LINE =                  '−−−−−−−−≺@TomenBots≻\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '↦ <b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '↦ <b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '↦ <b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '⇢ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '⇢ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '⇢ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '↦ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '↦ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '↦ <b>Files: </b>{Files}\n'
    RCPATH =                '↦ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '↦ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '⇢ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>✓ ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{Name}</code>\n'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n<b>» <a href="https://t.me/Hari_OP">{Bar}</a></b>'
    PROCESSED =         '\n<b>» ᴘʀᴏᴄᴇssᴇᴅ :</b> <code>{Processed}</code>'
    STATUS =            '\n<b>» sᴛᴀᴛᴜs :</b> <b><a href="{Url}">{Status}</a></b>'
    ETA =                                                ' | <b>ᴇᴛᴀ :</b> <code>{Eta}</code>'
    SPEED =             '\n<b>» sᴘᴇᴇᴅ :</b> <code>{Speed}</code>'
    ELAPSED =                                     ' | <b>ᴇʟᴀᴘsᴇᴅ :</b> <code>{Elapsed}</code>'
    ENGINE =            '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'
    STA_MODE =          '\n<b>» ᴍᴏᴅᴇ :</b> <code>{Mode}</code>'
    SEEDERS =           '\n<b>» sᴇᴇᴅᴇʀs :</b> <code>{Seeders}</code> | '
    LEECHERS =                                           '<b>ʟᴇᴇᴄʜᴇʀs :</b> <code>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>» sɪᴢᴇ : </b><code> {Size}</code>'
    SEED_SPEED =     '\n<b>» sᴘᴇᴇᴅ : </b> <code>{Speed}</code> | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅᴇᴅ :</b> <code>{Upload}</code>'
    RATIO =          '\n<b>» ʀᴀᴛɪᴏ : </b> <code>{Ratio}</code> | '
    TIME =                                         '<b>ᴛɪᴍᴇ : </b> <code>{Time}</code>'
    SEED_ENGINE =    '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>» sɪᴢᴇ : </b><code> {Size}</code>'
    NON_ENGINE =     '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n<b>» ᴜsᴇʀ :</b> <code>{User}</code> | '
    ID =                                                        '<b>ɪᴅ :</b> <code>{Id}</code>'
    BTSEL =          '\n<b>» sᴇʟᴇᴄᴛ :</b> <code>{Btsel}</code>'
    CANCEL =         '\n<b>» ᴄᴀɴᴄᴇʟ :</b> <code>{Cancel}</code>\n\n'

    ####------FOOTER--------
    FOOTER = '<u><b>ʙᴏᴛ sᴛᴀᴛs</b></u>\n\n'
    TASKS =  '<b>» ᴛᴀsᴋs :</b> <code>{Tasks}</code>\n'
    BOT_TASKS = '<b>» ᴛᴀsᴋs :</b> <code>{Tasks}/{Ttask}</code> | <b>ᴀᴠʟ :</b> <code>{Free}</code>\n'
    Cpu = '<b>» ᴄᴘᴜ :</b> <code>{cpu}%</code> | '
    FREE =                      '<b>ғʀᴇᴇ :</b> <code>{free} [{free_p}%]</code>'
    Ram = '\n<b>» ʀᴀᴍ :</b> <code>{ram}%</code> | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>'
    DL = '\n<b>» ᴅʟ :</b> <code>{DL}/s</code> | '
    UL =                        '<b>ᴜʟ :</b> <code>{UL}/s</code>'
    
    ###--------BUTTONS-------
    PREVIOUS = '⇇ ʙᴀᴄᴋ'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = 'ɴᴇxᴛ ⇉'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n↦\n'
    COUNT_SIZE = '↦ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '↦ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '↦ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '↦ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '↦ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
↦ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
↦ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<b><u>ᴜsᴇʀ sᴇᴛᴛɪɴɢs</u>
        
✦ ɴᴀᴍᴇ : {NAME} ( <code>{ID}</code> )
✦ ᴜsᴇʀ ɴᴀᴍᴇ : {USERNAME}
✦ ᴛᴇʟᴇɢʀᴀɴ ᴅᴄ : {DC}
✦ ʟᴀɴɢᴜᴀɢᴇ : {LANG}

🫅 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'''

    UNIVERSAL = '''<b><u>𝗨𝗡𝗜𝗩𝗘𝗥𝗦𝗔𝗟 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 : {NAME}</u>
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵

╔════❰ ꪮꪑᦋ ᥊ ᨶꪶꪮꪊᦔ ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼ 𝓨𝓣-𝓓𝓛𝓟 𝓞𝓹𝓽𝓲𝓸𝓷𝓼  : {YT}
║┣⪼ 𝓓𝓪𝓵𝓲𝔂 𝓣𝓪𝓼𝓴𝓮 : {DT}
║┣⪼ 𝓛𝓪𝓼𝓽 𝓑𝓸𝓽 𝓤𝓼𝓮𝓭  : {LAST_USED}
║┣⪼ 𝓤𝓼𝓮𝓻 𝓢𝓮𝓼𝓼𝓲𝓸𝓷  : {USESS}
║┣⪼ 𝓜𝓮𝓭𝓲𝓪𝓲𝓷𝓯𝓸 𝓜𝓸𝓭𝓮  : {MEDIAINFO}
║┣⪼ 𝓢𝓪𝓿𝓮 𝓜𝓸𝓭𝓮  : {SAVE_MODE}
║┣⪼ 𝓤𝓼𝓮𝓻 𝓑𝓸𝓽 𝓟𝓶  : {BOT_PM}
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>'''

    MIRROR = '''<b><u>𝗠𝗜𝗥𝗥𝗢𝗥 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 : {NAME}</u>
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵


╔════❰ ꪮꪑᦋ ᥊ ᨶꪶꪮꪊᦔ ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼ 𝓡𝓬𝓵𝓸𝓷𝓮 𝓒𝓸𝓷𝓯𝓲𝓰  : {RCLONE}
║┣⪼ 𝓜𝓲𝓻𝓻𝓸𝓻 𝓟𝓮𝓻𝓯𝓲𝔁  : {MPREFIX}
║┣⪼ 𝓜𝓲𝓻𝓻𝓸𝓻 𝓢𝓾𝓯𝓯𝓲𝓬  : {MSUFFIX}
║┣⪼ 𝓜𝓲𝓻𝓻𝓸𝓻 𝓡𝓮𝓶𝓷𝓪𝓶𝓮  : {MREMNAME}
║┣⪼ 𝓓𝓓𝓛 𝓢𝓮𝓻𝓿𝓮𝓻(𝓢)  : {DDL_SERVER}
║┣⪼ 𝓤𝓼𝓮𝓻 𝓣𝓓 𝓜𝓸𝓭𝓮  : {TMODE}
║┣⪼ 𝓣𝓸𝓽𝓪𝓵 𝓤𝓼𝓮𝓻 𝓣𝓓(𝓢)  : {USERTD}
║┣⪼ 𝓓𝓪𝓲𝓵𝔂 𝓛𝓮𝓮𝓬𝓱  : {DL} ᴘᴇʀ ᴅᴀʏ
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>'''

    LEECH = '''<b><b><u>𝗟𝗘𝗘𝗖𝗛 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 - {NAME}</u></b>
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵

╔════❰ ꪮꪑᦋ ᥊ ᨶꪶꪮꪊᦔ ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼ 𝓓𝓪𝓲𝓵𝔂 𝓛𝓮𝓮𝓬𝓱  : {DL} ᴘᴇʀ ᴅᴀʏ
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓣𝔂𝓹𝓮  : {LTYPE} 
║┣⪼ 𝓒𝓾𝓼𝓽𝓸𝓶 𝓣𝓱𝓾𝓶𝓫𝓷𝓪𝓲𝓵  : {THUMB}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓢𝓹𝓵𝓲𝓽 𝓢𝓲𝔃𝓮  : {SPLIT_SIZE}
║┣⪼ 𝓔𝓺𝓾𝓪𝓵 𝓢𝓹𝓵𝓲𝓽𝓼  : {EQUAL_SPLIT}
║┣⪼ 𝓜𝓮𝓭𝓲𝓪 𝓖𝓻𝓸𝓾𝓹  : {MEDIA_GROUP}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓒𝓪𝓹𝓽𝓲𝓸𝓷  : {LCAPTION}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓟𝓻𝓮𝓯𝓲𝔁  : {LPREFIX}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓢𝓾𝓯𝓯𝓲𝔁  : {LSUFFIX}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓓𝓾𝓶𝓹𝓼  : {LDUMP}
║┣⪼ 𝓛𝓮𝓮𝓬𝓱 𝓡𝓮𝓶𝓷𝓪𝓶𝓮  : {LREMNAME}
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>'''
