Summary:	xrefresh application
Summary(pl.UTF-8):	Aplikacja xrefresh
Name:		xorg-app-xrefresh
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrefresh-%{version}.tar.bz2
# Source0-md5:	1228f890f86148e4e6ae22aa73118cbb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrefresh application.

%description -l pl.UTF-8
Aplikacja xrefresh.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xrefresh
%{_mandir}/man1/xrefresh.1x*
