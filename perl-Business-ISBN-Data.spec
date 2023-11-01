#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: 250a666
#
Name     : perl-Business-ISBN-Data
Version  : 20231031.001
Release  : 56
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-Data-20231031.001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-Data-20231031.001.tar.gz
Summary  : 'data pack for Business::ISBN'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-Business-ISBN-Data-license = %{version}-%{release}
Requires: perl-Business-ISBN-Data-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Business-ISBN-Data package.
Group: Development
Provides: perl-Business-ISBN-Data-devel = %{version}-%{release}
Requires: perl-Business-ISBN-Data = %{version}-%{release}

%description dev
dev components for the perl-Business-ISBN-Data package.


%package license
Summary: license components for the perl-Business-ISBN-Data package.
Group: Default

%description license
license components for the perl-Business-ISBN-Data package.


%package perl
Summary: perl components for the perl-Business-ISBN-Data package.
Group: Default
Requires: perl-Business-ISBN-Data = %{version}-%{release}

%description perl
perl components for the perl-Business-ISBN-Data package.


%prep
%setup -q -n Business-ISBN-Data-20231031.001
cd %{_builddir}/Business-ISBN-Data-20231031.001
pushd ..
cp -a Business-ISBN-Data-20231031.001 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Business-ISBN-Data
cp %{_builddir}/Business-ISBN-Data-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Business-ISBN-Data/555b0f6fad9a85a3a0fa5de4f0e00103109cdf38 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Business::ISBN::Data.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Business-ISBN-Data/555b0f6fad9a85a3a0fa5de4f0e00103109cdf38

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
