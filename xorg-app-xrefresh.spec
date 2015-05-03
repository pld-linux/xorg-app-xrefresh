Summary:	xrefresh application to refresh all or part of an X screen
Summary(pl.UTF-8):	Aplikacja xrefresh do odświeżania całości lub części ekranu X
Name:		xorg-app-xrefresh
Version:	1.0.5
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrefresh-%{version}.tar.bz2
# Source0-md5:	a896382bc53ef3e149eaf9b13bc81d42
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrefresh application is a simple X program that causes all or part of
your screen to be repainted.

%description -l pl.UTF-8
Aplikacja xrefresh to prosty program X powodujący ponowne narysowanie
całości lub części ekranu.

%prep
%setup -q -n xrefresh-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xrefresh
%{_mandir}/man1/xrefresh.1*
