# 🐳 Docker Compose Lab

Bu proje, bir DevOps eğitim ortamı olarak Flask, Redis, ve Nginx bileşenlerini Docker Compose ile ayağa kaldıran basit bir örnektir.

##  Bileşenler

- **Flask (Python)** – Basit bir web uygulaması
- **Redis** – Sayaç verisini tutan in-memory veri tabanı
- **Nginx** – Ters proxy olarak Flask uygulamasına gelen istekleri yönlendirir
- **Docker Compose** – Tüm servisleri tek komutla ayağa kaldırır

## Kurulum

Ön koşullar:

- Docker
- Docker Compose (v1.29+)
- Git

### 1. Projeyi klonla

<pre><code>git clone https://github.com/yahusgame/docker-compose-lab.git</code>

cd docker-compose-lab 
</code></pre>

### 2. Uygulamayı başlat

<pre><code>vagrant up
  
vagrant ssh 

cd /home/vagrant/compose-lab

docker-compose up --build</code></pre>



## Bu komut 3 servisi başlatır:

- Flask app (5000 portunda)

- Redis

- Nginx (80 portunda → localhost erişimi)


### 3. Test et

Tarayıcıda (Host makinenin):

<pre><code>http://localhost:8080
</code></pre>

Her sayfa yenilemede, sayaç artacaktır. Redis bağlantısı üzerinden sayım yapılır.

# 🛠 Geliştirici Notları

### Redis bağlantısı test etmek için:

<pre><code>docker exec -it compose-lab_web_1 redis-cli -h redis ping
</code></pre>

### Flask kodu güncellendiğinde:

<pre><code>docker-compose up --build
</code></pre>

ile yeniden build alınmalıdır.

### Temizleme
<pre><code>docker-compose down</code></pre> 

# Katkı ve Geliştirme

Bu ortam, Docker, Vagrant, Kubernetes gibi DevOps bileşenlerine giriş amaçlı tasarlanmıştır.

Geliştirme yaparken öneri veya katkılar için pull request gönderilebilir.
