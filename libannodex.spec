%define	major 1
%define libname %mklibname annodex %{major}
%define develname %mklibname annodex -d

Summary:	Library for annotating and indexing networked media
Name:		libannodex
Version:	0.7.3
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD
URL:		http://www.annodex.net/
Source0:	http://www.annodex.net/software/libannodex/download/%{name}-%{version}.tar.bz2
Patch0:		libannodex.man.patch
Patch1:		libannodex-0.7.3-gcc4.diff
Patch2:		libannodex-0.7.3-avoid-version.diff
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	liboggz-devel >= 0.9.1
BuildRequires:	libcmml-devel >= 0.8
BuildRequires:	libsndfile-devel
BuildRequires:	expat-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libannodex is a library to provide reading and writing of Annodex files and
streams.

%package -n	%{libname}
Summary:	Library for annotating and indexing networked media
Group:          System/Libraries

%description -n	%{libname}
libannodex is a library to provide reading and writing of Annodex files and
streams.

%package -n	%{develname}
Summary:	Files needed for development using libannodex
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname annodex 1 -d}

%description -n	%{develname}
libannodex is a library to provide reading and writing of Annodex files and
streams.

This package contains the header files and documentation needed for development
using libannodex.

%package	tools
Summary:	Various tools using the annotating and indexing networked media library
Group:		File tools

%description	tools
This package contains various tools using the annotating and indexing networked
media library.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
rm -f configure
libtoolize --copy --force; aclocal -I m4; autoconf; automake

%configure2_5x

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/libannodex

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*
%dir %{_libdir}/annodex/importers
%{_libdir}/annodex/importers/*.so

%files -n %{develname}
%defattr(-,root,root)
%doc doc/libannodex/html/* TODO
%dir %{_includedir}/annodex
%{_includedir}/annodex/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/annodex/importers/*.a
%{_libdir}/annodex/importers/*.la
%{_libdir}/pkgconfig/annodex.pc

%files tools
%defattr(-,root,root)
%{_bindir}/anx*
%{_mandir}/man1/*
