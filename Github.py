from github import Github

#Hesabımıza Giriş Yapıyoruz.

try:
    git_hesap = Github("K_Adı", "Sifre")
    #print("Hesabınıza başarı ile giriş yapıldı.")
except:
    print("Hesabınıza giriş başarısız!")

#Githubda arama yapmak ve çıktı almak.
try:
    repos = git_hesap.search_repositories(query="language:python")
    print("Arama yapılıyor..")
    for repo in repos:
        print(repo)
except:
    print("Arama yapılamadı!")


#Profilde bulunan repolarınızın ismini almak.
try:
    for repo in git_hesap.get_user().get_repos():
        print(repo.name)
except:
    print("Kullanıcıya ait repo isimleri alınamadı!")




#Spesifik projeyi almak
try:
    repo = git_hesap.get_repo("Vitaee/PythonileSesliAsistanV2")

#Belirlenen projenin yıldız sayısını almak.
    print(repo.stargazers_count)
except:
    print("Hata işlem başarısız!")



#Belirlenen projeye kaç kişi baktığını görmek.
try:
    repo = git_hesap.get_repo("Vitaee/PythonileSesliAsistanV2")

    traff = repo.get_views_traffic()
    print(traff)

except:
    print("Proje bilgilerine erişilemedi!")


#Belirlenen projede bulunan dosyaları görmek.
try:
    repo = git_hesap.get_repo("Vitaee/PythonileSesliAsistanV2")
    content = repo.get_contents("")
    for content_fil in content:
        print(content_fil)
except:
    print("Hata!")

#Yeni bir proje oluşturmak.

try:
    user = git_hesap.get_user()
    repo = user.create_repo("deneme")
except:
    print("Repo oluşturulamadı!")

#Oluşturulan projeye dosya eklemek.
try:
    repo.create_file("test.txt", "commit","deneme yapıyorum")
except:
    print("Dosya ekleme işlemi başarısız oldu!")


#Oluşturulan projeyi silmek.
try:
    repo = git_hesap.get_repo("Vitaee/deneme")
    cont = repo.get_contents("test.txt")
    repo.delete_file(cont.path,"remove deneme", cont.sha, branch="master")
    print("Dosya silme işlemi başarı ile tamamlandı!")
except:
    print("Dosya silme işlemi başarısız!")
