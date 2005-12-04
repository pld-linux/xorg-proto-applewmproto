Summary:	AppleWM extension headers
Summary(pl):	Nag³ówki rozszerzenia AppleWM
Name:		xorg-proto-applewmproto
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/applewmproto-%{version}.tar.bz2
# Source0-md5:	3e63ff6ff6dd74a0adf419aa3c7d61b0
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
%setup -q -n applewmproto-%{version}

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/applewmproto.pc
