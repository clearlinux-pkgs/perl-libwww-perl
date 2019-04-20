#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-libwww-perl
Version  : 6.38
Release  : 38
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-6.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-6.38.tar.gz
Summary  : 'The World-Wide Web library for Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-libwww-perl-bin = %{version}-%{release}
Requires: perl-libwww-perl-license = %{version}-%{release}
Requires: perl-libwww-perl-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(File::Listing)
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(HTML::HeadParser)
BuildRequires : perl(HTTP::Cookies)
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Negotiate)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Net::HTTP)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::RequiresInternet)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Escape)
BuildRequires : perl(WWW::RobotRules)

%description
As of libwww-perl v6.02 you need to install the LWP::Protocol::https module
from its own separate distribution to enable support for https://... URLs for
LWP::UserAgent.

%package bin
Summary: bin components for the perl-libwww-perl package.
Group: Binaries
Requires: perl-libwww-perl-license = %{version}-%{release}

%description bin
bin components for the perl-libwww-perl package.


%package dev
Summary: dev components for the perl-libwww-perl package.
Group: Development
Requires: perl-libwww-perl-bin = %{version}-%{release}
Provides: perl-libwww-perl-devel = %{version}-%{release}
Requires: perl-libwww-perl = %{version}-%{release}

%description dev
dev components for the perl-libwww-perl package.


%package license
Summary: license components for the perl-libwww-perl package.
Group: Default

%description license
license components for the perl-libwww-perl package.


%package man
Summary: man components for the perl-libwww-perl package.
Group: Default

%description man
man components for the perl-libwww-perl package.


%prep
%setup -q -n libwww-perl-6.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-libwww-perl
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-libwww-perl/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/LWP.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Authen/Basic.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Authen/Digest.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Authen/Ntlm.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/ConnCache.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Debug.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Debug/TraceHTTP.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/DebugFile.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/MemberMixin.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/cpan.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/data.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/file.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/ftp.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/gopher.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/http.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/loopback.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/mailto.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/nntp.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/nogo.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/RobotUA.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.2/LWP/UserAgent.pm
/usr/lib/perl5/vendor_perl/5.28.2/libwww/lwpcook.pod
/usr/lib/perl5/vendor_perl/5.28.2/libwww/lwptut.pod

%files bin
%defattr(-,root,root,-)
/usr/bin/lwp-download
/usr/bin/lwp-dump
/usr/bin/lwp-mirror
/usr/bin/lwp-request

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP.3
/usr/share/man/man3/LWP::Authen::Ntlm.3
/usr/share/man/man3/LWP::ConnCache.3
/usr/share/man/man3/LWP::Debug.3
/usr/share/man/man3/LWP::MemberMixin.3
/usr/share/man/man3/LWP::Protocol.3
/usr/share/man/man3/LWP::RobotUA.3
/usr/share/man/man3/LWP::Simple.3
/usr/share/man/man3/LWP::UserAgent.3
/usr/share/man/man3/libwww::lwpcook.3
/usr/share/man/man3/libwww::lwptut.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-libwww-perl/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lwp-download.1
/usr/share/man/man1/lwp-dump.1
/usr/share/man/man1/lwp-mirror.1
/usr/share/man/man1/lwp-request.1
