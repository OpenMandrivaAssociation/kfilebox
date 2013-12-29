%define qmake /usr/lib/qt4/bin/qmake -makefile 
%define debug_package          %{nil}

Name: kfilebox
Summary: KDE front-end for Dropbox
Version: 0.4.9
Release: 4
License: GPLv2
Group: Networking/File transfer 
Source0: http://sourceforge.net/projects/kdropbox/files/%{name}-%{version}/Source/%{name}_%{version}.tar.gz
Url: http://kdropbox.deuteros.es/

BuildRequires: gcc-c++ 
BuildRequires: make
BuildRequires: pkgconfig(Qt3Support)
BuildRequires: qt4-linguist
BuildRequires: kdelibs4-devel

%description
KDE front-end for Dropbox. This is free software, but it requires the
proprietary dropbox daemon that will be downloaded at first run.

%prep
%setup -q -n %{name}_%{version}

%build
%qmake  
%make

%install

install -D -m 755 bin/%name %{buildroot}%{_bindir}/%name
install -D -m 644 img/%{name}.png %{buildroot}%{_datadir}/%{name}/%name
install -d %{buildroot}%{_datadir}/icons/hicolor/
cp -r img/hicolor/* %{buildroot}%{_datadir}/icons/hicolor/
install -D -m 644 locale/ar/kfilebox.mo %{buildroot}%{_datadir}/locale/ar/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/br/kfilebox.mo %{buildroot}%{_datadir}/locale/br/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/cs/kfilebox.mo %{buildroot}%{_datadir}/locale/cs/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/el/kfilebox.mo %{buildroot}%{_datadir}/locale/el/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/en/kfilebox.mo %{buildroot}%{_datadir}/locale/en/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/en/kfilebox.mo %{buildroot}%{_datadir}/locale/en_GB/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/de/kfilebox.mo %{buildroot}%{_datadir}/locale/de_DE/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/es/kfilebox.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/fr/kfilebox.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/gl/kfilebox.mo %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/it/kfilebox.mo %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/lt/kfilebox.mo %{buildroot}%{_datadir}/locale/lt/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/nl/kfilebox.mo %{buildroot}%{_datadir}/locale/nl/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/pl/kfilebox.mo %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/ru/kfilebox.mo %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/si/kfilebox.mo %{buildroot}%{_datadir}/locale/si/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/tr/kfilebox.mo %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/zh/kfilebox.mo %{buildroot}%{_datadir}/locale/zh/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/zh/kfilebox.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/kfilebox.mo
install -D -m 644 locale/tw/kfilebox.mo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/kfilebox.mo
install -d %{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/autostart/ %{buildroot}%{_datadir}/apps/%{name}/

%find_lang %name

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
GenericName=%{name}
Comment=KDE front end for Dropbox
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Network;FileTransfer;
EOF

cat > %{buildroot}%{_datadir}/autostart/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=kfilebox
GenericName=kfilebox
Comment=KDE front end for Dropbox
Exec=%{_bindir}/kfilebox
Icon=kfilebox
Terminal=false
Type=Application
StartupNotify=false
Categories=Network;FileTransfer;
X-KDE-autostart-after=panel
X-KDE-StartupNotify=false
X-DBUS-StartupType=Unique
X-KDE-UniqueApplet=true
X-KDE-autostart-condition=kfileboxrc:General:AutoStart:false
EOF


cat > %{buildroot}%{_datadir}/apps/%{name}/%{name}.notifyrc << EOF
[Global]
Comment=Kfilebox
Name=kfilebox
IconName=kfilebox

[Event/notify]
Name=Notification
Comment=Any notification
Action=Popup
EOF

%files -f %name.lang 
%dir %{_datadir}/kfilebox  
%doc doc/readme.txt  
%{_datadir}/applications/kfilebox.desktop  
%{_datadir}/autostart/kfilebox.desktop  
%{_datadir}/apps/kfilebox/*  
%{_datadir}/kfilebox/*
%{_bindir}/kfilebox
%{_datadir}/icons/hicolor/16x16/apps/kfilebox.png
%{_datadir}/icons/hicolor/22x22/apps/kfilebox.png
%{_datadir}/icons/hicolor/24x24/apps/kfilebox.png
%{_datadir}/icons/hicolor/32x32/apps/kfilebox.png
%{_datadir}/icons/hicolor/48x48/apps/kfilebox.png
%{_datadir}/icons/hicolor/64x64/apps/kfilebox.png
%{_datadir}/icons/hicolor/128x128/apps/kfilebox.png
