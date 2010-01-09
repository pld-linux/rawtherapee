#
Summary:	THe Experimental RAw Photo Editor
Summary(pl.UTF-8):	THe Experimental RAw Photo Editor - eksperymentalny edytor zdjęć RAW
Name:		rawtherapee
Version:	3.0
%define	_milestone	a1
%define	_rel		1
Release:	0.%{_milestone}.%{_rel}
#Release:	0.1
License:	distributable ?
Group:		X11/Applications/Graphics
Source0:	http://www.rawtherapee.com/%{name}30%{_milestone}.tgz
# Source0-md5:	673056cb7269ac98a762581efe1c8c3b
#Source0:	http://www.rawtherapee.com/%{name}241.tgz
Source1:	%{name}.desktop
Source2:	TODO
NoSource:	0
URL:		http://www.rawtherapee.com/
Requires:	gtk+2 >= 2:2.10
# this version _requires_ SSE
Requires:	cpuinfo(sse)
Suggests:	adobe-ICC-profiles
# because of SSE
ExclusiveArch:	i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
Raw Therapee is a free RAW converter and digital photo processing
software.

%description -l pl.UTF-8
Raw Therapee to darmowy konwerter z formatu RAW oraz narzędzie do
przetwarzania zdjęć cyfrowych.

%prep
%setup -q -n RawTherapee30a1
cp %{SOURCE2} PLD-TODO
chmod -R u+w *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}%{_libdir},%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_appdir}/{images,languages,profiles,themes}

install options rt *.so $RPM_BUILD_ROOT%{_appdir}
install images/* $RPM_BUILD_ROOT%{_appdir}/images
install languages/* $RPM_BUILD_ROOT%{_appdir}/languages
install profiles/* $RPM_BUILD_ROOT%{_appdir}/profiles
install themes/* $RPM_BUILD_ROOT%{_appdir}/themes

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << 'EOF'
#!/bin/sh
cd %{_appdir}
exec ./rt
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/logoicon32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PLD-TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/rt
%attr(755,root,root) %{_appdir}/*.so
# Makes rt crash sometimes.
#%{_appdir}/options
%dir %{_appdir}/images
%{_appdir}/images/*.png
%dir %{_appdir}/languages
%{_appdir}/languages/*
%dir %{_appdir}/profiles
%{_appdir}/profiles/*.pp2
%dir %{_appdir}/themes
%{_appdir}/themes/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
