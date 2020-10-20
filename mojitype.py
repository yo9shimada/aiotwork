import regex

def moji_type(moji):
    # 初期値
    code = 0
    # 数字
    code = 1 if str.isdecimal(moji) else code
    # アルファベット
    p = regex.compile('[a-zA-Zａ-ｚＡ-Ｚ]')
    code = 2 if p.fullmatch(moji) else code
    # ひらがな
    p = regex.compile('\p{Hiragana}')    
    code = 3 if p.fullmatch(moji) else code
    # カタカナ
    p = regex.compile('\p{Katakana}')    
    code = 4 if p.fullmatch(moji) else code
    # 半角記号
    p = regex.compile('[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]')
    code = 5 if p.fullmatch(moji) else code
    # 全角記号
    p = regex.compile('[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]')
    code = 6 if p.fullmatch(moji) else code
    # 漢字
    p = regex.compile(r'\p{Script_Extensions=Han}')
    code = 7 if p.fullmatch(moji) else code
    return (code)

def separate_tango(sentence):
    tango = ""
    t_list = []
    pre_moji = ""
    pre_cord = 0
    for m in moji:
        cord = moji_type(m)
        if cord != pre_cord and pre_cord != 0:
            t_list.append(tango)
            tango = ""
        tango += m
        pre_cord = cord
    t_list.append(tango)
    return (t_list)
        
print(separate_tango("aaaあああ"))