Summary:	Tuning application for DVB cards
Name:		dvbtune
Version:	0.5
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://downloads.sourceforge.net/dvbtools/%{name}-%{version}.tar.gz
# Source0-md5:	5212564c786f2538db753214e0e21473
URL:		http://dvbtools.sourceforge.net/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple tuning application for DVB cards.

%prep
%setup -q

%build
%{__make} %{name} xml2vdr \
	CFLAGS="%{rpmcflags} -I%{_includedir}/libxml2 -DNEWSTRUCT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} xml2vdr $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc scripts README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/xml2vdr
