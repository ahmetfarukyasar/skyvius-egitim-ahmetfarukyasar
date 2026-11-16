``` mermaid
flowchart LR
    %% Güç Yolu
    Batarya["<b>Batarya</b><br/>Enerji sağlar"] ==>|"Güç"| ESC["<b>ESC</b><br/>Motoru sürer"]
    ESC ==>|"Güç"| Motor["<b>Motor</b><br/>İtki üretir"]

    %% Bilgi Yolu
    Alici["<b>Alıcı</b><br/>Pilot komutunu taşır"] -.->|"Bilgi"| UK["<b>Uçuş Kontrolcüsü</b><br/>İtkiyi hesaplar"]
    Telemetri["<b>Telemetri</b><br/>Yer istasyonuyla haberleşir"] <-.->|"Bilgi"| UK
    UK -.->|"Komut"| ESC

    Kamera["<b>Kamera</b><br/>Görüntü alır"] -.->|"Bilgi"| GorevPC["<b>Görev Bilgisayarı</b><br/>Görüntüyü işler"]
    GorevPC -.->|"Bilgi"| UK
```