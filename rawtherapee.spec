Summary:	THe Experimental RAw Photo Editor
Summary(pl.UTF-8):	THe Experimental RAw Photo Editor - eksperymentalny edytor zdjęć RAW
Name:		rawtherapee
Version:	4.2
Release:	1
License:	GPLv3 and MIT and IJG
Group:		X11/Applications/Graphics
Source0:	http://rawtherapee.com/shared/source/%{name}-%{version}.tar.xz
# Source0-md5:	e6510ed56fdc35aa712b4c0f54c52ac0
Source1:	%{name}.desktop
Patch0:		%{name}-4.2-appstreamtweak.patch
Patch1:		%{name}_CVE-2015-3885.patch
URL:		http://www.rawtherapee.com/
BuildRequires:	appstream-glib
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	fftw3-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	gtkmm-devel >= 2.16
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	fftw3
Requires:	gtk+2 >= 2:2.10
Requires:	hicolor-icon-theme
Suggests:	adobe-ICC-profiles
# https://fedorahosted.org/fpc/ticket/530
# to find: `grep Revision: rawtherapee-4.2/rtengine/dcraw.c`
Provides:	bundled(dcraw) = 1.467
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rawtherapee is a RAW image processing software. It gives full control
over many parameters to enhance the raw picture before finally
exporting it to some common image format.

%description -l pl.UTF-8
Raw Therapee to darmowy konwerter z formatu RAW oraz narzędzie do
przetwarzania zdjęć cyfrowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# fix wrong line endings
%undos LICENSE.txt

# Remove mercurial dependency and specify version
cat > rtgui/version.h << EOF
#ifndef _VERSION_
#define _VERSION_

#define VERSION "%{version}"
#define TAGDISTANCE 0
#define CACHEFOLDERNAME "RawTherapee${CACHE_NAME_SUFFIX}"
#endif
EOF

cat > AboutThisBuild.txt << EOF
See package information
EOF

%build
%cmake \
	-DLIBDIR=%{_libdir} \
	-DAUTOMATED_BUILD_SYSTEM:BOOL=ON \
	-DCACHE_NAME_SUFFIX="" \
	-DCMAKE_BUILD_TYPE=release \
	-DCMAKE_CXX_FLAGS_RELEASE="%{rpmcxxflags}" \
	-DCMAKE_C_FLAGS_RELEASE="%{rpmcflags}" \
	.
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32}/apps

# These file are taken from the root already
rm -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt LICENSE.txt RELEASE_NOTES.txt
%attr(755,root,root) %{_bindir}/rawtherapee
%{_mandir}/man1/rawtherapee.1*
%attr(755,root,root) %{_libdir}/librtengine.so
%attr(755,root,root) %{_libdir}/librtexif.so
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
