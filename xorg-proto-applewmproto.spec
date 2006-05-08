Summary:	AppleWM extension headers
Summary(pl):	Nag³ówki rozszerzenia AppleWM
Name:		xorg-proto-applewmproto
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/applewmproto-%{version}.tar.bz2
# Source0-md5:	d5d7c69837cc7dcbf2aa181ff423ab20
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppleWM extension headers.

%description -l pl
Nag³ówki rozszerzenia AppleWM.

%package devel
Summary:	AppleWM extension headers
Summary(pl):	Nag³ówki rozszerzenia AppleWM
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
AppleWM extension headers.

%description devel -l pl
Nag³ówki rozszerzenia AppleWM.

%prep
%setup -q -n applewmproto-X11R7.0-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/applewmproto.pc
