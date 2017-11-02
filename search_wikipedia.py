import wikipedia

def wikipediaSearch(search_text):
    response_string = ''
    wikipedia.set_lang('ja')
    search_response = wikipedia.search(search_text)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            response_string = 'アワ、アワワワ…\n　エラー、エラー\n' + e.message + '\n' + str(e)
        response_string = '説明するよ。\n'
        response_string += wiki_page.content[0:100] + '.....だよ。\n'
        response_string += wiki_page.url
    else:
        response_string = 'その用語は登録されてないみたい、だよ\n'
    return response_string

if __name__ == "__main__":
    print(wikipediaSearch('アイマス'))
