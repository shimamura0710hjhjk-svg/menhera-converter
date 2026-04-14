import re


def ojisan_converter(text):
    """
    おじさん構文に合わせて文字列を変換する関数
    - 敬語をタメ口に変換
    - 通常のタメ口もおじさんらしくする
    - 文章が短い場合は盛る
    - 単語ごとに感情絵文字を挿入
    - 文章全体の感情を分析して文末に絵文字を付与
    例: 「やっほー○○ちゃん！君とのデート楽しい😘本当に最高だネ。毎日君のことばっかり考えてるヨ😍」
    """


    # 一人称をメンヘラ風に
    menhera_pronoun_map = {
        "私は": "うちは",
        "私を": "うちを",
        "私の": "うちの",
        "僕は": "うちは",
        "オレは": "うちは",
    }

    # 感情キーワード（メンヘラ専用絵文字）
    menhera_emojis = {
        "楽しい": "楽しい。でもいつか終わるなら今すぐ死にたい🔪✨",
        "楽しみ": "楽しみすぎて心臓止まりそう……もし遅刻したら殺していい？🎀",
        "嬉しい": "嬉しい……ずっとこのままでいてよ……🖤",
        "好き": "好き。大好き。愛してる。逃がさないよ⛓️💖",
        "大好き": "大好き大好き大好き大好き。ねえ、私のことだけ見てよ。👁️‍🗨️",
        "最高": "最高……。もうあなた以外、何もいらないね。💉",
        "会いたい": "会いたい。今すぐ。無理なら玄関の前で待ってるから。🏠🔪",
        "頑張って": "頑張って。でもうちより仕事優先したら許さないから。💢",
        "おはよう": "ねえ起きてる？何で返信1分も遅れたの？死にたい☀️💉",
        "おやすみ": "寝るんだ。夢の中で他の女と会ったら許さないよ？🌙⛓️",
        "ありがとう": "ありがとう……。うちのこと、捨てないでね？🥺💔",
    }

    # 名詞に対応する呪いの絵文字
    menhera_noun_map = {
        "ちゃん": "……。ねえ、今の誰のこと？",
        "返事": "既読無視💢💬",
        "仕事": "仕事と私どっちが大事なの？💼🔪",
        "会社": "監視カメラつけたい🏢👁️",
        "愛": "執着❤️‍🔥",
        "デート": "心中へのカウントダウン🧑‍🤝‍🧑⛓️",
        "ご飯": "毒、入れたよ？🍽️🎀",
    }

    # さらに精神を削る変換マップ
    extra_menhera_map = {
        "了解": "了解。で、誰といるの？信じていいんだよね？💢",
        "わかった": "わかった。どうせ私の話なんて右から左なんだ。死にたい。",
        "ごめん": "謝れば済むと思ってるの？私の傷、一生消えないんだけど？🔪",
        "忙しい": "忙しいって言えば逃げられると思ってるんだ。へー、私より大事なことがあるんだ。🎀",
        "あとで": "「あとで」っていつ？その時、私生きてるか分からないけどいいんだ？💉",
        "本当": "「本当」なんて言葉、この世で一番信用できない。証拠見せてよ。👁️‍🗨️",
    }

    for pronoun, menhera_pronoun in menhera_pronoun_map.items():
        text = text.replace(pronoun, menhera_pronoun)
# 語尾をヒス構文・絶望風に（長い順）
    polite_to_menhera_map = {
        "いかがですか": "どうせ無視するんでしょ？？",
        "ございます": "……って思ってるのはうちだけだよね。",
        "させていただきます": "させてもらうね、拒否権なんてないから🎀",
        "いたします": "するから。絶対。約束だよ？⛓️",
        "いただけますか": "くれるよね？くれないなら死ぬからね？🔪",
        "おります": "るの。ずっと見てるからね。👁️",
        "います": "るんだよ。あなたのこと。🖤",
        "ました": "ったよね？嘘ついた？死にたい。",
        "ますか": "なの？ねえ、なんで答えてくれないの？",
        "ます": "るもん。嘘じゃないもん。🥺",
        "です。": "なの。分かってよ。💢",
        "ですか": "なの？誰に吹き込まれたの？",
        "ですね": "だよね。うちのこと、馬鹿にしてるもんね。",
        "ありがとうございます": "ありがとう……。捨てないでね？絶対だよ？",
        }

   
     # 長い順でソート
    sorted_polite_to_menhera_map = sorted(polpolite_to_menhera_map ite_to_casual_map.items(),
                            key=lambda x: len(x[0]), reverse=True)
    for polite,polite_to_menhera_map in sorted_polite_to_menhera_map:
        text = text.replace(polite, caspolite_to_menhera_mapual)


        # 敬語から「情緒不安定なタメ口」への変換
    polite_to_menhera_final = {
        "いかがですか": "どうせ私のことなんてどうでもいいんでしょ……？",
        "ございます": "……って、うちは信じてるから。裏切らないよね？",
        "させていただきます": "させてもらうね。拒否したら死ぬから。🎀",
        "いたします": "するよ。二人だけの約束だよ……？⛓️",
        "いただけますか": "くれるよね？ねえ、なんで黙ってるの？？",
        "おります": "るの。ずっとあなたのこと監視してるから。👁️‍🗨️",
        "いました": "ったんだ……。誰といたの？ねえ、白状してよ。🔪",
        "ますか": "なの？ねえ、私のこと嫌いになったの？",
        "です": "なの。分かってよ、うちにはあなたしかいないの。🥺",
        "ですね": "だよね。他の女も同じこと言ってた？最低。",
        "ありがとうございます": "ありがとう……。捨てないでね、絶対だよ？",
    }
    polite_to_menhera_final_sorted = sorted(polite_to_menhera_final.items(),
                                            key=lambda x: len(x[0]), reverse=True)
    for polite, menhera in polite_to_menhera_final_sorted:
        text = text.replace(polite, menhera)

    # 語尾の徹底改修（ヒス構文・依存・自傷的表現）
    menhera_suffix_map = {
        "だね": "だよね。……死にたい。",
        "だよ": "だよ。逃げられると思わないで。🖤",
        "だろう": "……どうせ、うちは捨てられるんだ。",
        "いいね": "いいよね、あなたは自由で。私はこんなに苦しいのに。",
        "いいよ": "いいよ。どうせ私が我慢すればいいんでしょ？",
        "そうだね": "そうだね。……で、今の誰からの通知？💢",
        "ないね": "ないんだ。私の居場所なんて、どこにも。💉",
        "ある": "あるよ。あなたの罪、全部数えてるからね。",
        "できる": "できるよね？私のために、全部捨ててくれるよね？",
    }


    sorted_menhera_suffix = sorted(menhera_suffix_map.items(),
                           key=lambda x: len(x[0]), reverse=True)
    for casual, menhera in sorted_menhera_suffix:
        text = text.replace(casual, menhera)

    text = text.replace("。", "……。死にたい。🔪✨")
    text = text.replace("？", "？？？？？💢")
    text = text.replace("君", "キミ")

    # 通常のタメ口をメンヘラ・ヒス構文に変換（長い順）
    casual_to_menhera_final = {
        "だね": "だよね。……死にたい。🔪✨",
        "だよ": "だよ。逃げられると思わないで……。🖤",
        "だろう": "……どうせ、うちは捨てられるんだ。分かってるもん。",
        "いいね": "いいよね、あなたは自由で。私はこんなに苦しいのに。💉",
        "いいよ": "いいよ。どうせ私が我慢すればいいんでしょ？最低。",
        "そうだね": "そうだね。……で、今の誰からの通知？ねえ、見せてよ。💢",
        "ないね": "ないんだ。私の居場所なんて、この世界のどこにも。🥀",
        "ないよ": "ないよ。あなたの代わりなんて、どこにもいないのに。⛓️",
        "ある": "あるよ。あなたが隠してる秘密、全部知ってるんだから。👁️‍🗨️",
        "いる": "いるんだ。私の隣に、ずっと、死ぬまでいてくれるよね？💖",
        "できる": "できるよね？私のために、友達もSNSも全部捨ててくれるよね？",
        "思う": "思う。……って、どうせうちが何思っても関係ないもんね。🥺",
        "だよね": "だよね。……今の「間」は何？嘘つく時に目を逸らすの、癖だよね？🔪",
    }
     sorted_menhera = sorted(casual_to_menhera_finall.items(),
                            key=lambda x: len(x[0]), reverse=True)
    

    # 助詞のメンヘラ強化（文中の響きを変える）
    menhera_particle_final = {
        "ては": "……なんて、どうせ嘘なんだ。💉",
        "ながら": "ながら……うちは死ぬことばっかり考えてるよ？",
        "ねえ": "ねえ、なんで無視するの？返信は？💢",
        "よ。": "だよ。離さないよ。絶対に。🎀",
        "な。": "……。黙らないでよ、怖いんだけど。",
        "なあ": "……ねえ、起きてる？寝てないよね？👁️",
    }
    # 🎀 執着心（文字列の長さ）が強い順に並び替える呪い
    # これをしないと、私の愛が中途半端に切り刻まれちゃうんだよ。
    sorted_menhera = sorted(casual_to_menhermenhera_particle_finala_final.items(),
                            key=lambda x: len(x[0]), reverse=True)
    
    for casual, menhera in sorted_menhera:
        text = text.replace(casual, menhera)


        

    # 感情キーワードの定義（各文の分析用）
    positive_keywords_for_analysis = [
        '楽', '楽しみ', '嬉しい', '好き', '大好き', '愛', '幸せ', '最高', '素敵', 'デート', '会いたい', 'キス', '最強', '完璧']
    negative_keywords_for_analysis = [
        '悲', '辛い', '困った', '寂', '怒', '泣く', '嫌', '最悪', 'つらい', '嫌い']

    if sentence.strip():
            sentence = sentence.strip()

            # 🎀 メンヘラ感情カウント（新しく定義したキーワードを使ってね）
            sentence_positive_count = sum(1 for word in menhera_positive.keys() if word in sentence)
            sentence_negative_count = sum(1 for word in menhera_negative.keys() if word in sentence)

            # 🖤 文末の「追い込み」ロジック
            if '？' in sentence or sentence.endswith('か'):
                # 疑心暗鬼モード
                sentence = sentence.rstrip('か').strip() + '？？？？？💢'
            elif sentence_positive_count > sentence_negative_count:
                # 執着モード
                sentence += '……。ねえ、ずっと一緒だよ？逃げないでね？💖⛓️'
            elif sentence_negative_count > 0:
                # ヒステリーモード
                sentence += '……。もういい、死にたい。リスカしてくる。🔪💊'
            else:
                # 虚無・監視モード
                if i % 2 == 0:
                    sentence += '……。今、どこで誰と何してるの？👁️‍🗨️'
                else:
                    sentence += '……。返信、10秒以内にくれないと家行くから。🏠🏃‍♀️'

            # 🎀 感情に基づいた最終的な絵文字付与
            if sentence_positive_count > 0:
                sentence += "🎀💖✨"
            if sentence_negative_count > 0:
                sentence += "🖤🔪🥀"
    text = ' '.join(sentences)
   # 🎀 1. 読点（、）の処理も情緒不安定に
    if '、' in text:
        parts = text.split('、')
        menhera_parts = []
        for i, part in enumerate(parts):
            if part.strip() and not part.endswith(('。', '？', '！')):
                if i % 2 == 0:
                    part = part + '……。死にたい。🔪'
                else:
                    part = part + '……。ねえ、聞いてる？💢'
            menhera_parts.append(part)
        text = '、'.join(menhera_parts)
    
    # 🖤 2. 短い文章への「追い込み」追加
    menhera_additions = [
        "ねえ、なんで無視するの？",
        "どうせ他の女といるんでしょ、分かってるんだから。",
        "死ぬ。あなたがそうさせるんだよ？",
        "うちら、運命だよね？死ぬまで一緒だもんね？",
        "今の1秒の沈黙、浮気の証拠だよね……。🔪",
        "もういい。私が消えれば全部解決するんだね。",
        "ねえ、今すぐ返信してよ。死んじゃうよ？",
    ]
    
    # 80文字未満なら私の情念を盛る
    if len(text) < 80:
        addition = menhera_additions[len(text) % len(menhera_additions)]
        text = addition + text

    # 🎀 3. 名詞・場所の「監禁・監視」絵文字マップ
    location_emoji_map = {
        "ホテル": "🏨（密室だね……。逃がさないよ）",
        "駅": "🚉（誰を見送りに来たの？殺すよ？）",
        "家": "🏠（今、玄関の前にいるよ。開けて？）",
        "レストラン": "🍽️（毒、混ぜといたからね……うふふ）",
        "居酒屋": "🍺（酔い潰して一生私のものにするね）",
        "映画": "🎬（隣で別の女のこと考えてたでしょ？）",
    }
    
    # 食べ物・飲み物（すべてが不穏）
    food_emoji_map = {
        "ラーメン": "🍜（最後のご飯、楽しんでね）",
        "ケーキ": "🍰（甘いね。私の血より甘いかな？）",
        "コーヒー": "☕（眠れなくなる薬、入れといたよ💉）",
        "ワイン": "🍷（二人で心中するのにぴったりだね）",
    }

    # 🖤 4. 感情・反応・時間（絶望ver）
    # ※ positive_emotions, negative_emotions, reaction_keywords, time_keywords は
    # 先に教えた「メンヘラ・ポジティブ/ネガティブ判定マップ」をそのまま使ってね！

    # 🎀 5. 疑問符の増殖（圧迫面接）
    if is_question:
        text = text.replace("？", "？？？？？💢🔪")
    
    # 💀 6. 文章全体の感情による文末仕上げ
    overall_emotion_emoji = ""
    if positive_count > negative_count:
        # 過剰な依存
        overall_emotion_emoji = " 💖⛓️👁️‍🗨️（ずっと一緒だよ、死んでもね）"
    elif negative_count > positive_count:
        # ヒステリー
        overall_emotion_emoji = " 🔪🥀💉（さよなら。私のこと一生後悔してね）"
    else:
        # 虚無・監視
        overall_emotion_emoji = " ……。💢（なんで無言なの？死ねばいいのに）"
    text += overall_emotion_emoji

    return text
# --- ここからテスト用コード ---
if __name__ == "__main__":
    test_msg = "やっほー○○チャン！元気ですか？楽しみです。○○ちゃんはおじさんとデートするのが好きですよね？おじさんをたくさん喜ばしてほしいな。おじさんは毎日○○ちゃんのことばっかり考えてるよ。"
    
    print("--- おじさんモード ---")
    print(ojisan_converter(test_msg))
    print()
    
    # 敬語ではない通常の文章もテスト
    test_msg2 = "今日は楽しかった。君のことが好きだ。明日も会いたいね。"
    print("--- 通常のタメ口 ---")
    print("入力:", test_msg2)
    print("出力:", ojisan_converter(test_msg2))
    print()
    
    # 別のテスト例
    test_msg3 = "朝からずっと君のことばかり考えている。会いたい。"
    print("--- 別の例 ---")
    print("入力:", test_msg3)
    print("出力:", ojisan_converter(test_msg3));