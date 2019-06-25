from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import os
import unidecode
#os.getcwd()
#os.chdir("C:/Users/Caio Laptop/Documents/Repositories/campo-blotter")
urls = ["http://www.thecolgatemaroonnews.com/news/article_0d761634-9eeb-11e7-ad3a-1fb9f54b1245.html",
        "http://www.thecolgatemaroonnews.com/news/article_4f258116-30df-11e7-bf54-0bb96a62758c.html",
        "http://www.thecolgatemaroonnews.com/news/article_b5c89902-25dc-11e7-9509-034dc39566cc.html",
        "http://www.thecolgatemaroonnews.com/news/article_5d2eccd6-205e-11e7-a7b6-030f080e8aa4.html",
        "http://www.thecolgatemaroonnews.com/news/article_ee4ac216-1ae0-11e7-aa80-4f53cf4911fa.html",
        "http://www.thecolgatemaroonnews.com/news/article_053cf3e4-154c-11e7-8e0a-afdc0f4ac568.html",
        "http://www.thecolgatemaroonnews.com/news/article_67eb28ee-0fde-11e7-b5b2-978da95c8cc9.html",
        "http://www.thecolgatemaroonnews.com/news/article_cf74ed32-04e5-11e7-ae6c-236339942978.html",
        "http://www.thecolgatemaroonnews.com/news/article_6b241bee-ff65-11e6-9fa0-1b5281aa95cf.html",
        "http://www.thecolgatemaroonnews.com/news/article_3bdd8272-f9e7-11e6-a014-5fab1e5309da.html",
        "http://www.thecolgatemaroonnews.com/news/article_2bf7dcee-f466-11e6-858c-67b2d3efeb5a.html",
        "http://www.thecolgatemaroonnews.com/news/article_de9aa638-eeee-11e6-9a24-f30b38d6d2ae.html",
        "http://www.thecolgatemaroonnews.com/news/article_2085c21a-e965-11e6-bc24-ffc26d8ad389.html",
        "http://www.thecolgatemaroonnews.com/news/article_08cb87a4-ad0b-11e6-93dd-2b0fbfc5ca10.html",
        "http://www.thecolgatemaroonnews.com/news/article_6d0dc5d2-a76c-11e6-94df-b38011565d49.html",
        "http://www.thecolgatemaroonnews.com/news/article_6795b03e-a1df-11e6-bae3-c74e519dd4f7.html",
        "http://www.thecolgatemaroonnews.com/news/article_6795b03e-a1df-11e6-bae3-c74e519dd4f7.html",
        "http://www.thecolgatemaroonnews.com/news/article_e4138746-8bdf-11e6-b06f-3f69099d93b5.html",
        "http://www.thecolgatemaroonnews.com/news/article_fcd8865a-8662-11e6-973b-4fa10ed3f389.html",
        "http://www.thecolgatemaroonnews.com/news/article_b175e768-80de-11e6-b5dd-4bf0633372a4.html",
        "http://www.thecolgatemaroonnews.com/news/article_f874a028-7b61-11e6-8aa2-8f85e503a289.html",
        "http://www.thecolgatemaroonnews.com/news/article_1cda194e-75df-11e6-bd90-df9bc2cdfee8.html",
        "http://www.thecolgatemaroonnews.com/news/article_90d6bdea-7056-11e6-8e51-e7a855270661.html",
        "http://www.thecolgatemaroonnews.com/news/article_ae0ec9c8-ea21-11e4-83f2-dbea94df07e7.html",
        "http://www.thecolgatemaroonnews.com/news/article_2ed5f176-e518-11e4-b94f-1725aa828653.html",
        "http://www.thecolgatemaroonnews.com/news/article_77a4266e-e31c-11e4-850f-b343a331de41.html",
        "http://www.thecolgatemaroonnews.com/news/article_7b08e384-db25-11e4-92e2-e7126b5ca14e.html",
        "http://www.thecolgatemaroonnews.com/news/article_46459c94-d41a-11e4-a406-8b196193f53c.html",
        "http://www.thecolgatemaroonnews.com/news/article_8341ccce-c39b-11e4-889d-f32b57c9a648.html",
        "http://www.thecolgatemaroonnews.com/news/article_5ebdd5cc-be1a-11e4-a0e8-0b9f0c858450.html",
        "http://www.thecolgatemaroonnews.com/news/article_324bcc1a-b7da-11e4-9929-b306b5c61c3d.html",
        "http://www.thecolgatemaroonnews.com/news/article_486a6708-b33a-11e4-afe8-b3fb13982fb3.html",
        "http://www.thecolgatemaroonnews.com/news/article_e7d77842-ad97-11e4-ad2a-57e2932efdfa.html",
        "http://www.thecolgatemaroonnews.com/news/article_880d3f3a-a812-11e4-8ef1-27b28bfc2331.html",
        "http://www.thecolgatemaroonnews.com/news/article_5e55e314-a1d6-11e4-a1df-ef4cd0ca43ca.html",
        "http://www.thecolgatemaroonnews.com/news/article_5f74889c-a4f9-11e4-b2fa-875b00a0e3ed.html",
        "http://www.thecolgatemaroonnews.com/news/article_e743988a-a684-11e4-bf5e-237ab2ae0e3c.html",
        "http://www.thecolgatemaroonnews.com/news/article_78b57a12-aa37-11e4-a8a6-5fe50ecbc8fb.html",
        "http://www.thecolgatemaroonnews.com/news/article_f38345f6-abec-11e4-b6ff-cb0d1a2e3861.html",
        "http://www.thecolgatemaroonnews.com/news/article_0493c010-ab1a-11e4-81de-e39c4507d191.html",
        "http://www.thecolgatemaroonnews.com/news/article_65993b94-a983-11e4-afb9-bfdffd8308ee.html",
        "http://www.thecolgatemaroonnews.com/news/article_c3b12d7c-a97e-11e4-b666-3b84b55ba372.html",
        "http://www.thecolgatemaroonnews.com/news/article_c3b12d7c-a97e-11e4-b666-3b84b55ba372.html",
        "http://www.thecolgatemaroonnews.com/news/article_9c73328a-a507-11e4-8655-6fd8d70b01c1.html",
        "http://www.thecolgatemaroonnews.com/news/article_056b96ea-a2a8-11e4-906a-e3361562096d.html"]

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    body_text = soup.find("div", itemprop="articleBody")
    return body_text.text


f = open("blotter.txt", "w")
for url in urls:
    body = urllib.request.urlopen(url).read()
    body_text = text_from_html(body)
    body_text = body_text.partition("TNCMS")[0] + body_text.partition(";")[2]
    body_text = unidecode.unidecode(body_text)
    # strip newlines
    body_text = re.sub("\n","",body_text)
    # strip date/time stamps
    body_text = re.sub(" a.m.: | p.m.: ", "", body_text)
    body_text = re.sub("(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday),","",body_text)
    # escape commas
    #body_text = re.sub(",","",body_text)
    # remove last timestamp and add comma for CSV
    body_text = re.sub(r"(| |  |   )\d{1,2}:\d{2}","\n",body_text)
    body_text = re.sub(r"(| |  |   )\d{1,2}/\d{1,2}","",body_text)
    body_text = re.sub("\d{1,2}\,","",body_text)
    f.write(body_text)

f.close()
