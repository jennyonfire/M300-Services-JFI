# M300 - Dokumentation von Dennis Allenspach, Jenifer Fischer &amp; Jan Gantenbein
Im Modul 300 wurde uns die Arbeit mit Containers und Virtuellen Maschienen näher gebracht.
## Auftrag
Unser Auftrag war es, verschiedene Services via Vagrant und GitHub zu realisieren. Mit Vagrant kann man mit einem Vagrant-File eine VM erstellen ohne irgendwelche        konfigurationen zu machen. Alles befindet sich in diesem File. IaC
## Bewertung
* Umgebung (Multi VM) funktionsfähig auf eigenem Notebook (Note 4.0)
* Bestehende VM aus Vagrant Cloud zum laufen bringen (Note 4.5)
* Eigener Service auf Basis IaC implementieren (Note 5.0 – 5.5)
* Projekt auf github Ablegen und Dokumentieren (Markdown) (Note 5.5 – 6.0)

![Kompetenzen](https://github.com/Dionysos376/M300-Services/blob/master/Kompetenz_Bewertung.PNG)
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
Wir haben bei dem Auftrag des eigenen Services zuerst darauf geschaut, dass wir das Vagrantfile überhaupt verstehen.


> ##### Unser Vagrantfile:
> Test Vagrantfile
## Testing
Um das Testing durchzuführen haben wir verschiedene Testcases aufgeschrieben und nach diesen Fällen die Tests druchgeführt.
Das erwartete Ergebniss und das tatsächliche ErgebnisS wurde dann dokumentiert und festgehalten.

**|Test|** <br> _Erwartete Ausgabe_ <br>  _Tatsächliches Ausgabe_

**|Erstellung VM|** <br>  _ttt_ <br> _ttt_

**|SSH Verbindung|** <br> _ttt_ <br> _ttt_

**|Benutzer erstellung|** <br> _ttt_ <br> _ttt__

**|Sicherheit|** <br> _ttt_ <br> _ttt__
