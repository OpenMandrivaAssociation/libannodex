%define	major 1
%define libname %mklibname annodex %{major}
%define develname %mklibname annodex -d

Summary:	Library for annotating and indexing networked media
Name:		libannodex
Version:	0.7.3
Release:	9
Group:		System/Libraries
License:	BSD
URL:		http://www.annodex.net/
Source0:	http://www.annodex.net/software/libannodex/download/%{name}-%{version}.tar.bz2
Patch0:		libannodex.man.patch
Patch1:		libannodex-0.7.3-gcc4.diff
Patch2:		libannodex-0.7.3-avoid-version.diff
Patch3:		libannodex-malloc_fix.diff
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	liboggz-devel >= 0.9.1
BuildRequires:	libcmml-devel >= 0.8
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	expat-devel

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
%patch3 -p0

%build
rm -f configure
libtoolize --copy --force --ltdl; aclocal -I m4; autoconf; automake

%configure2_5x --disable-static

%make

%check
make check

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/libannodex

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
%{_libdir}/pkgconfig/annodex.pc

%files tools
%defattr(-,root,root)
%{_bindir}/anx*
%{_mandir}/man1/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-8mdv2011.0
+ Revision: 609733
- rebuild

* Fri May 21 2010 Frederic Crozat <fcrozat@mandriva.com> 0.7.3-7mdv2010.1
+ Revision: 545651
- rebuild with latest liboggz

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.7.3-6mdv2010.0
+ Revision: 429716
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-5mdv2009.0
+ Revision: 229605
- added P3 to make it build (-lm)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.3-4mdv2008.0
+ Revision: 89832
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-3mdv2008.0
+ Revision: 83568
- new devel naming


* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-2mdv2007.0
+ Revision: 94087
- bump release
- fix deps (expat-devel)
- Import libannodex

* Mon Aug 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-1mdv2007.0
- initial Mandriva package (fc5 extras import)
- added P1 from debian
- added P2 to avoid the version in the module file names

