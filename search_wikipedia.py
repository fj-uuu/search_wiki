import wikipedia

def wikipediaSearch(text):
    response_string = ''
    wikipedia.set_lang('ja')
    index = text.find('って何')
    search_text = text[0:index]
    search_response = wikipedia.search(search_text)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            try:
                wiki_page = wikipedia.page(search_response[1])
            except Exception as e:
                response_string = 'アワ、アワワワ…\n　エラー、エラー\n' + e.message + '\n' + str(e)
        response_string = '説明するよ。\n'
        response_string += wiki_page.content[0:100] + '.....だよ。\n'
        response_string += wiki_page.url
    else:
        response_string = 'その用語は登録されてない、よ。\nごめんね。'

    return response_string

if __name__ == "__main__":
    print(wikipediaSearch('アイマスって何？'))
