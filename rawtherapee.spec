# TODO:
# - check the license if its distributable...
# - gtkrc and options should be marked as config and moved to /etc ?
Summary:	THe Experimental RAw Photo Editor
Name:		rawtherapee
Version:	2.2
Release:	1
License:	distributable ?
Group:		X11/Applications/Graphics
Source0:	http://www.rawtherapee.com/%{name}22_glibc24.tgz
# NoSource0-md5:	eba5b474a750abf41ab406cc25989349
Source1:	%{name}.desktop
URL:		http://www.rawtherapee.com/
# is it ok?
Suggests:	uname(sse)
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
Raw Therapee is a free RAW converter and digital photo processing software.

%prep
%setup -q -n RawTherapee
chmod -R u+w *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_appdir}/{images,profiles}

install gtkrc options rt $RPM_BUILD_ROOT%{_appdir}
install images/* $RPM_BUILD_ROOT%{_appdir}/images
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
%{_appdir}/gtkrc
%{_appdir}/options
%dir %{_appdir}/images
%{_appdir}/images/*.png
%dir %{_appdir}/profiles
%{_appdir}/profiles/*.pp2
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
