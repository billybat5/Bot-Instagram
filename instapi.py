import re
from time import sleep
from instagrapi import Client
class Instapi:
    def url_cls(self, url):
        if not '?' in url:
            pattern = r"(.+)\?"
            URL = re.match(pattern, url+'?').group(1)
            return URL
        else:
            pattern = r"(.+)\?"
            URL = re.match(pattern, url).group(1)
            return URL
    def return_resource(self, url):
        cl = Client()
        USERNAME, PASSWORD = 'm6caownv', 'privateSecurity10#'

        print('Esperar 7 Segundos')
        sleep(7)
        print('Great!\n')
        cl.login(USERNAME, PASSWORD)
        URL = cl.media_pk_from_url(self.url_cls(url))
        datos = cl.media_info(URL).dict()

        if 'resources' in datos and len(datos['resources']) != 0:
            # string = ''
            # for counter in range(0, len(datos['resources'])):
            #     string += str(datos['resources'][counter]['thumbnail_url']) + ' '
            # return string

            lista = []
            for counter in range(0, len(datos['resources'])):
                lista.append(f'Imagen {counter + 1} -> ' + str(datos['resources'][counter]['thumbnail_url']))
            return lista


        elif len(datos['clips_metadata']) == 0:
            return datos['image_versions2']['candidates'][0]['url']
        return str(datos['video_url'])