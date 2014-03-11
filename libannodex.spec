%define major 0
%define libname %mklibname annodex %{major}
%define devname %mklibname annodex -d

Summary:	Library for annotating and indexing networked media
Name:		libannodex
Version:	0.7.3
Release:	10
License:	BSD
Group:		System/Libraries
Url:		http://www.annodex.net/
Source0:	http://www.annodex.net/software/libannodex/download/%{name}-%{version}.tar.bz2
Patch0:		libannodex.man.patch
Patch1:		libannodex-0.7.3-gcc4.diff
Patch2:		libannodex-0.7.3-avoid-version.diff
Patch3:		libannodex-malloc_fix.diff
BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRequires:	pkgconfig(cmml)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(oggz)
BuildRequires:	pkgconfig(sndfile)
Conflicts:	%{_lib}annodex1 < 0.7.3-10

%description
libannodex is a library to provide reading and writing of Annodex files and
streams.

%files
%doc AUTHORS ChangeLog COPYING README
%dir %{_libdir}/annodex/importers
%{_libdir}/annodex/importers/*.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for annotating and indexing networked media
Group:		System/Libraries
Requires:	%{name}
Conflicts:	%{_lib}annodex1 < 0.7.3-10
Obsoletes:	%{_lib}annodex1 < 0.7.3-10

%description -n %{libname}
libannodex is a library to provide reading and writing of Annodex files and
streams.

%files -n %{libname}
%{_libdir}/libannodex.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Files needed for development using libannodex
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
libannodex is a library to provide reading and writing of Annodex files and
streams.

This package contains the header files and documentation needed for development
using libannodex.

%files -n %{devname}
%doc doc/libannodex/html/* TODO
%dir %{_includedir}/annodex
%{_includedir}/annodex/*.h
%{_libdir}/libannodex.so
%{_libdir}/pkgconfig/annodex.pc

#----------------------------------------------------------------------------

%package tools
Summary:	Various tools using the annotating and indexing networked media library
Group:		File tools

%description tools
This package contains various tools using the annotating and indexing networked
media library.

%files tools
%{_bindir}/anx*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
rm -f configure
libtoolize --copy --force --ltdl; aclocal -I m4; autoconf; automake --add-missing
#autoreconf -fi

%configure2_5x --disable-static
%make

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/libannodex

%check
make check

