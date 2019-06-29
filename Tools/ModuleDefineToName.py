import os

module_defines = [
'SCE_SYSMODULE_FIBER',
'SCE_SYSMODULE_ULT',
'SCE_SYSMODULE_NGS2',
'SCE_SYSMODULE_XML',
'SCE_SYSMODULE_NP_UTILITY',
'SCE_SYSMODULE_VOICE',
'SCE_SYSMODULE_VOICEQOS',
'SCE_SYSMODULE_NP_MATCHING2',
'SCE_SYSMODULE_NP_SCORE_RANKING',
'SCE_SYSMODULE_RUDP',
'SCE_SYSMODULE_NP_TUS',
'SCE_SYSMODULE_FACE',
'SCE_SYSMODULE_SMART',
'SCE_SYSMODULE_GAME_LIVE_STREAMING',
'SCE_SYSMODULE_COMPANION_UTIL',
'SCE_SYSMODULE_PLAYGO',
'SCE_SYSMODULE_FONT',
'SCE_SYSMODULE_VIDEO_RECORDING',
'SCE_SYSMODULE_S3DCONVERSION',
'SCE_SYSMODULE_AUDIODEC',
'SCE_SYSMODULE_JPEG_DEC',
'SCE_SYSMODULE_JPEG_ENC',
'SCE_SYSMODULE_PNG_DEC',
'SCE_SYSMODULE_PNG_ENC',
'SCE_SYSMODULE_VIDEODEC',
'SCE_SYSMODULE_MOVE',
'SCE_SYSMODULE_PAD_TRACKER',
'SCE_SYSMODULE_DEPTH',
'SCE_SYSMODULE_HAND',
'SCE_SYSMODULE_LIBIME',
'SCE_SYSMODULE_IME_DIALOG',
'SCE_SYSMODULE_NP_PARTY',
'SCE_SYSMODULE_FONT_FT',
'SCE_SYSMODULE_FREETYPE_OT',
'SCE_SYSMODULE_FREETYPE_OL',
'SCE_SYSMODULE_FREETYPE_OPT_OL',
'SCE_SYSMODULE_SCREEN_SHOT',
'SCE_SYSMODULE_NP_AUTH',
'SCE_SYSMODULE_SULPHA',
'SCE_SYSMODULE_SAVE_DATA_DIALOG',
'SCE_SYSMODULE_INVITATION_DIALOG',
'SCE_SYSMODULE_DEBUG_KEYBOARD',
'SCE_SYSMODULE_MESSAGE_DIALOG',
'SCE_SYSMODULE_AV_PLAYER',
'SCE_SYSMODULE_CONTENT_EXPORT',
'SCE_SYSMODULE_AUDIO_3D',
'SCE_SYSMODULE_NP_COMMERCE',
'SCE_SYSMODULE_MOUSE',
'SCE_SYSMODULE_COMPANION_HTTPD',
'SCE_SYSMODULE_WEB_BROWSER_DIALOG',
'SCE_SYSMODULE_ERROR_DIALOG',
'SCE_SYSMODULE_NP_TROPHY',
'SCE_SYSMODULE_NP_SNS_FACEBOOK',
'SCE_SYSMODULE_MOVE_TRACKER',
'SCE_SYSMODULE_NP_PROFILE_DIALOG',
'SCE_SYSMODULE_NP_FRIEND_LIST_DIALOG',
'SCE_SYSMODULE_APP_CONTENT',
'SCE_SYSMODULE_NP_SIGNALING',
'SCE_SYSMODULE_REMOTE_PLAY',
'SCE_SYSMODULE_USBD',
'SCE_SYSMODULE_GAME_CUSTOM_DATA_DIALOG',
'SCE_SYSMODULE_M4AAC_ENC',
'SCE_SYSMODULE_AUDIODEC_CPU',
'SCE_SYSMODULE_ZLIB',
'SCE_SYSMODULE_CONTENT_SEARCH',
'SCE_SYSMODULE_DECI4H',
'SCE_SYSMODULE_HEAD_TRACKER',
'SCE_SYSMODULE_SYSTEM_GESTURE',
'SCE_SYSMODULE_VIDEODEC2',
'SCE_SYSMODULE_AT9_ENC',
'SCE_SYSMODULE_CONVERT_KEYCODE',
'SCE_SYSMODULE_SHARE_PLAY',
'SCE_SYSMODULE_HMD',
'SCE_SYSMODULE_FACE_TRACKER',
'SCE_SYSMODULE_HAND_TRACKER',
'SCE_SYSMODULE_AUDIODEC_CPU_HEVAG',
'SCE_SYSMODULE_LOGIN_DIALOG',
'SCE_SYSMODULE_LOGIN_SERVICE',
'SCE_SYSMODULE_SIGNIN_DIALOG',
'SCE_SYSMODULE_JSON2',
'SCE_SYSMODULE_AUDIO_LATENCY_ESTIMATION',
'SCE_SYSMODULE_HMD_SETUP_DIALOG',
'SCE_SYSMODULE_VR_TRACKER',
'SCE_SYSMODULE_CONTENT_DELETE',
'SCE_SYSMODULE_IME_BACKEND',
'SCE_SYSMODULE_NET_CTL_AP_DIALOG',
'SCE_SYSMODULE_PLAYGO_DIALOG',
'SCE_SYSMODULE_SOCIAL_SCREEN',
'SCE_SYSMODULE_EDIT_MP4',
'SCE_SYSMODULE_TEXT_TO_SPEECH',
'SCE_SYSMODULE_BLUETOOTH_HID',
'SCE_SYSMODULE_VR_SERVICE_DIALOG',
'SCE_SYSMODULE_JOB_MANAGER',
'SCE_SYSMODULE_SOCIAL_SCREEN_DIALOG',
'SCE_SYSMODULE_NP_TOOLKIT2'
]

def walk(adr):
    mylist=[]
    for root,dirs,files in os.walk(adr):
        for name in files:
            adrlist=os.path.join(root, name)
            mylist.append(adrlist)
    return mylist

def main():
    flist = walk('system\common\lib')
    flist = [os.path.basename(x) for x in flist]
    module_list = [fname[:-10].lower() for fname in flist]
    mod_set = set(module_list)

    name_list = []
    for macro_name in module_defines:
        parts = macro_name[14:].split('_')
        parts = [item.capitalize() for item in parts]
        module_name = 'libSce' + ''.join(parts)
        if not module_name.lower() in mod_set:
            print('can not find:' + module_name);

        name_list.append((macro_name, module_name))

    with open('module_name_map.txt', 'w') as dst:
        for macro, name in name_list:
            line = '{{ {}, "{}" }},\n'.format(macro, name)
            dst.write(line)


    print('done')

if __name__ == '__main__':
    main()