# M300 - Dokumentation von Dennis Allenspach, Jennifer Fischer &amp; Jan Gantenbein
Im Modul 300 wurde uns die Arbeit mit Containers und Virtuellen Maschienen näher gebracht.
## Auftrag
Unser Auftrag war es, verschiedene Services via Vagrant und GitHub zu realisieren. Mit Vagrant kann man mit einem Vagrant-File eine VM erstellen ohne irgendwelche        konfigurationen zu machen. Alles befindet sich in diesem File. IaC
## Bewertung
* Umgebung (Multi VM) funktionsfähig auf eigenem Notebook (Note 4.0)
* Bestehende VM aus Vagrant Cloud zum laufen bringen (Note 4.5)
* Eigener Service auf Basis IaC implementieren (Note 5.0 – 5.5)
* Projekt auf github Ablegen und Dokumentieren (Markdown) (Note 5.5 – 6.0)

![Kompetenzen](https://github.com/Dionysos376/M300-Services/blob/master/Kompetenz_Bewertung.PNG)

## Netzwerkplan
![Netzwerkplan](https://github.com/Dionysos376/M300-Services/blob/master/Netzwerkplan.PNG)
## Unser Vorgehen
Wir arbeiteten nach dem IPERKA System. Wir schauten uns den Auftrag genau an und informierten uns über die verschiedenen Services. Anschliessen planten wir unser Vorgehen. Die Vorgehensweise wurde vom Auftragsdokument übernommen, da dort alles genau beschrieben wurde. Wir arbeiteten somit das Skript durch. Wir hatten Startprobleme, da es einige Zeit gedauert hat Django korrekt aufzusetzen. Es gab Probleme mit Versionen, welche Unkompatibel waren und zusätzich noch mit dem Anbinden am Vagrant File. Am Ende konnten wir es mit einem kleinem Umweg lösen indem wir auf einer Ubuntu Box manuell per Shell die benötigten Packages installieren und die Webapplikation via einem synced Folder direkt rüber geladen haben. Die Konfiguration von Django war sehr schwierig und die Zeit reichte nicht aus um sich das benötigte Wissen anzueignen, deswegen haben wir eine bereits erstellte Grundkonfiguration für eine Webapplikation benützt und diese nach unseren Wünschen angepasst. 
## Github
Wir haben uns Konten bei GITHUB erstellt. GITHUB bietet die Möglichkeit Dateien auf einfachem Wege hochzuladen, leicht bearbeitbar und offen zugänglich zu machen.
Mit Github ist es möglich den Kontakt zu anderen Entwickler auf der ganzen welt zu aufzubauen. Genau auf diesem Wege werden wir auch unsere fertigen Vagrantfiles mit unserem Lehrer kommunizieren.
> _“GitHub brings together the world’s largest community of developers to discover, share, and build better software.”_
## Produktive Nutzung
Unsere Umgebung ist darauf aufgebaut, dass man mit einem Command eine ganze VM Umgebung aufsetzen kann, die sich automatisch installiert und Konfiguriert. (Mit Ausnahme der IP welche Statisch vergeben worden ist, nach Angabe von Herr Berger)
Bsp. kann ein Informatiker, der mehrere VMs pro Tag aufsetzten muss sich sehr viel Arbeit, Zeit und Nerven sparen.
So kann er mit Git Bash in ein Verzeichnis gehen, wo sich ein Vagrant-File befindet. In diesem Verzeichnis kann er ganz einfach den command “vagrant up” ausführen und das Vagrant-File wird ausgeführt.
In diesem Vagrant-File ist definiert von wo er sich das OS runterladen soll, welche konfigurationen er vornehemen soll und wie ist installiert wird.
## Eigener Service
Wir haben bei dem Auftrag des eigenen Services zuerst darauf geschaut, dass wir das Vagrantfile überhaupt verstehen. Unser Service beeinhaltet eine Webapplikation, welche mit Django aufgesetzt wurde. Django ist ein Framework von Python. Auf der Website kann man User erstellen und sich mit diesen Anmelden. Weiterhin gibt es einen Admin Account, welcher alle Users verwalten kann. Der Service wurde realtiv einfach aufgesetzt, und zwar wurde im Vagrantfile ein verknüpfter Ordner definiert welcher die ganze Django konfiguration beeinhaltet. Der Service ist mit Django Kentnissen sehr einfach ausbaufähig.

## Nutzung:
Um das Vagrant File effektiv zu nutzen sollte zuerst die Firewall aktiviert werden. Für das muss man die VM mit Vagrant up starten, danach mittels ssh Verbindung die Firewall aktivieren "sudo ufw enable" und anschliesslich wieder im Website Verzeichnis "vagrant/github" die Seite starten. "python3 manage.py runserver 0:8000"


> ##### Unser Vagrantfile:
> Das Vagrantfile finden sie in unserem jeweiligen Repository <br>
> Dennis Allenspach: M300-Services <br>
> Jennifer Fischer: M300-Services-JFI <br>
> Jan Gantenbein: M300-Services-LB1
## Testing
Um das Testing durchzuführen haben wir verschiedene Testcases aufgeschrieben und nach diesen Fällen die Tests druchgeführt.
Das erwartete Ergebniss und das tatsächliche ErgebnisS wurde dann dokumentiert und festgehalten.

**|Test|** <br> _Erwartete Ausgabe_ <br>  _Tatsächliches Ausgabe_

**|Erstellung VM|** <br>  _-Die VM soll mit "vagrant up" erstellt werden (Nach den Angaben des Vagrant Files)_ <br> _-Die VM wird erfolgreich erstellt (mit den richtigen Konfigurationen)_

**|SSH Verbindung|** <br> _-Es soll eine SSH Verbindung auf die neu erstelte VM möglich sein_ <br> _-Die SSH Verbindung (Port 22) konnte erfolgreich etabliert werden_

**|Benutzer erstellung|** <br> _-Es soll ein Benutzer erstellt werden (Nach den eigenen Eingaben)_ <br> _-Es wird ein Benutzer erstellt, mit den eingegebenen Daten_

**|Admin Account|** <br> _-Der Benutzer Admin kann über die Website /admin user erstellen und löschen_ <br> _-Benutzer können beliebig erstellt und gelöscht werden_

**|Sicherheit|** <br> _Wir haben die VM mit der Standard Firewall von Unix (UFW) aufgesetzt. Diese dann so konfiguriert dass der Port 8000, für jeden und Port 22, für unseren jeweiligen lokalen Host offen ist_

## Team-Reflexion
Die Anfänge mit Vagrant waren recht einfach für uns, da Dennis Allenspach das Thema sehr gut verstand und Jennifer Fischer und Jan Gantenbein das Thema gut erklären konnte.
Von Anfang an wurden die Aufgabenbereiche unterteilt, so dass die Arbeit recht schnell voranging.
Bei der weiteren Arbeit war nicht Vargant das Problem, sondern bis man die Installation von Django richtig verstand.
Die letzt Hürde war das Implementieren der Firewall, da diese einen Manuellen Befehl benötigte, welcher aus unerklärlichen Gründen nicht umgangen werden konnte.
