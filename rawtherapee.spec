# TODO:
# - check the license if its distributable...
# - gtkrc and options should be marked as config and moved to /etc ?
# attached gtkrc is full of bugs and does not fit to system theme.
#
Summary:	THe Experimental RAw Photo Editor
Summary(pl.UTF-8):	THe Experimental RAw Photo Editor - eksperymentalny edytor zdjęć RAW
Name:		rawtherapee
Version:	2.3
Release:	1
License:	distributable ?
Group:		X11/Applications/Graphics
Source0:	http://www.rawtherapee.com/%{name}23_glibc24.tgz
# NoSource0-md5:	0789f0dbfedfe39173470a33a7a55125
Source1:	%{name}.desktop
NoSource:	0
URL:		http://www.rawtherapee.com/
Requires:	gtk+2 >= 2:2.10
# this version _requires_ SSE, but it doesn't work...
#Requires:	uname(sse)
Suggests:	adobe-ICC-profiles
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
Raw Therapee is a free RAW converter and digital photo processing
software.

%description -l pl.UTF-8
Raw Therapee to darmowy konwerter z formatu RAW oraz narzędzie do
przetwarzania zdjęć cyfrowych.

%prep
%setup -q -n RawTherapee%{version}
chmod -R u+w *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_appdir}/{images,languages,profiles}

install options rt $RPM_BUILD_ROOT%{_appdir}
install images/* $RPM_BUILD_ROOT%{_appdir}/images
install languages/* $RPM_BUILD_ROOT%{_appdir}/languages
install profiles/* $RPM_BUILD_ROOT%{_appdir}/profiles

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
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
%attr(755,root,root) %{_bindir}/*
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/rt
%{_appdir}/options
%dir %{_appdir}/images
%{_appdir}/images/*.png
%dir %{_appdir}/languages
%{_appdir}/languages/*
%dir %{_appdir}/profiles
%{_appdir}/profiles/*.pp2
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
