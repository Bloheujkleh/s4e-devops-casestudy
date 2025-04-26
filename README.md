AI Code Generator
Bu proje, Flask tabanlı basit bir web arayüzü üzerinden kullanıcıdan alınan prompt’a göre Python kodu üreten bir yapay zekâ destekli asistan uygulamasıdır.

Özellikler
Kullanıcıdan alınan prompt'a göre Python kodu üretir.

Üretilen kodu başlık ve kod olarak iki parçaya ayırır.

OpenAI API kullanılarak model entegrasyonu sağlanmıştır.

Dockerize edilmiştir ve Minikube üzerinde çalıştırılmaya hazırdır.

Kubernetes için deployment.yaml dosyası hazırlanmıştır.

Kullanılan Teknolojiler
Python

Flask

OpenAI API

Docker

Kubernetes (Minikube)

Projeyi Çalıştırma
1. Docker Build
bash
Kopyala
Düzenle
docker build -t bulent1234/ai-code-generator:latest .
2. Docker Push
bash
Kopyala
Düzenle
docker push bulent1234/ai-code-generator:latest
3. Kubernetes Deployment
bash
Kopyala
Düzenle
kubectl apply -f deployment.yaml
Uygulama port 80 üzerinden erişilebilir.

DockerHub Image
DockerHub Image Link

📣 Açıklama:
Bu proje, S4E DevOps Stajyer Aday Görevi kapsamında geliştirilmiştir.
Prompt alıp, ilgili Python kodu ve kısa başlık üreten bir AI asistanıdır.

