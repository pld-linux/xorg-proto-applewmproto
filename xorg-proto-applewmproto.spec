Summary:	AppleWM extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia AppleWM
Name:		xorg-proto-applewmproto
Version:	1.2.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/applewmproto-%{version}.tar.bz2
# Source0-md5:	44e18d01857f9dfeb8628e317e786f31
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppleWM extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia AppleWM.

%package devel
Summary:	AppleWM extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia AppleWM
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
AppleWM extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia AppleWM.

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/applewm*.h
%{_pkgconfigdir}/applewmproto.pc
