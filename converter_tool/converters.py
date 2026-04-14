import re

def menhera_converter(text):
    # 一人称を「うち」に固定
    menhera_pronoun_map = {
        "私は": "うちは", "私を": "うちを", "私の": "うちの",
        "僕は": "うちは", "オレは": "うちは", "自分は": "うちは"
    }
    for p, mp in menhera_pronoun_map.items():
        text = text.replace(p, mp)

    # 🎀 感情・状況マップ（長い順にソートして使うよ）
    menhera_map = {
        # 敬語・タメ口変換
        "いかがですか": "どうせ無視するんでしょ？？",
        "ございます": "……。ねえ、聞いてる？",
        "いたします": "するから。絶対。約束だよ？⛓️",
        "ますか": "なの？ねえ、なんで答えてくれないの？",
        "です": "なの。分かってよ。🔪",
        "だね": "だよね。……死にたい。✨",
        "だよ": "だよ。逃げられると思わないで。🖤",
        
        # 感情キーワード
        "楽しい": "楽しい。でもいつか終わるなら今すぐ死にたい🔪✨",
        "楽しみ": "楽しみすぎて心臓止まりそう……。🎀",
        "嬉しい": "嬉しい……ずっとこのままでいてよ……🖤",
        "好き": "好き。大好き。愛してる。逃がさないよ⛓️💖",
        "大好き": "大好き大好き大好き。ねえ、私のことだけ見てよ。👁️‍🗨️",
        "最高": "最高……。あなたがいれば、もう何もいらないね。💉",
        "幸せ": "幸せ。幸せすぎて怖い。今すぐあなたを殺していい？❤️‍🔥",
        
        # ネガティブ
        "悲しい": "悲しい。あなたが息をしてるだけで、私以外の空気が混ざるのが悲しいの😭",
        "辛い": "辛い……。死にたい。リスカしてあなたの名前書くね？💉",
        "寂しい": "寂しい寂しい寂しい。誰と寝てるの？💢",
        "嫌い": "嫌い。大嫌い。死ね。……なんて言うと思った？一生苦しめてあげる🎀🖤",
        "不安": "不安でたまらないの。ねえ、私を捨てないって誓って。⛓️",
        
        # 反応・時間
        "わかった": "わかった。どうせ適当に返してるだけでしょ。🥺",
        "了解": "了解……。冷たいね。私のこと見捨てようとしてるんだ。💢",
        "明日": "明日。もし会えなかったら、あなたの家まで行くからね。🏠",
        "毎日": "毎日、毎分、毎秒。あなたのすべてを監視してるよ。✨",
    }

    # 長い順にソートして一気に置換（ここがエラーの元になりやすいから慎重に！）
    sorted_map = sorted(menhera_map.items(), key=lambda x: len(x[0]), reverse=True)
    for k, v in sorted_map:
        text = text.replace(k, v)

    # 🎀 助詞・句点の追い込み
    text = text.replace("。", "……。🔪✨")
    text = text.replace("？", "？？？？？💢")
    
    # 🖤 文末に「情緒不安定」な一言を強制追加
    additions = [
        "ねえ、なんで無視するの？",
        "死にたい。あなたがそうさせるんだよ？",
        "うちら、運命だよね？死ぬまで一緒だもんね？",
        "もういい。私が消えれば全部解決するんだね。",
    ]
    import random
    text += " " + random.choice(additions)

    return text



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
    sorted_polite_to_menhera_map =sorted(polite_to_menhera_map.items(),
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
        text = text.replace(polite, polite_to_menhera_map)

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

    # 通常のタメ口をメンヘラ・ヒス構文に変換（200行目付近の修正）
    casual_to_menhera_final = {
        "だね": "だよね。……死にたい。🔪✨",
        "だよ": "だよ。逃げられると思わないで……。🖤",
        "だろう": "……どうせ、うちは捨てられるんだ。分かってるもん。",
        "いいね": "いいよね、あなたは自由で。私はこんなに苦しいのに。💉",
        "いいよ": "いいよ。どうせ私が我慢すればいいんでしょ？最低。",
        "そうだね": "そうだね。……で、今の誰からの通知？ねえ、見せてよ。💢",
        "ないね": "ないんだ。私の居場所なんて、どこにも。🥀",
        "ないよ": "ないよ。あなたの代わりなんて、どこにもいないのに。⛓️",
    }
    
    # ↓ 200行目：ここ！先頭のスペースを周りと揃えてね！
    sorted_menhera_final = sorted(casual_to_menhera_final.items(),
                                  key=lambda x: len(x[0]), reverse=True)

    for casual, menhera in sorted_menhera_final:
        text = text.replace(casual, menhera)

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
    sorted_menhera = sorted(menhera_particle_final.items(),
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

# # テスト実行（エラーが出ないか確認してね）
# --- ここから下を全部これに書き換えて！ ---
if __name__ == "__main__":
    test_msg = "今日は楽しかった。また明日会いたいな。大好き。"
    print("--- メンヘラモード ---")
    print(menhera_converter(test_msg))