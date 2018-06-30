#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Business-ISBN-Data
Version  : 20140910.003
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-Data-20140910.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-Data-20140910.003.tar.gz
Summary  : 'data pack for Business::ISBN'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Business-ISBN-Data-man

%description
See the tests in the t/ directory for examples until I add some more.

%package man
Summary: man components for the perl-Business-ISBN-Data package.
Group: Default

%description man
man components for the perl-Business-ISBN-Data package.


%prep
%setup -q -n Business-ISBN-Data-20140910.003

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
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Business/ISBN/Data.pm
/usr/lib/perl5/site_perl/5.26.1/Business/ISBN/RangeMessage.xml
/usr/lib/perl5/site_perl/5.26.1/Business/ISBN/make_data.pl

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Business::ISBN::Data.3
