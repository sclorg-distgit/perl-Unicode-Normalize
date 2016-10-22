%{?scl:%scl_package perl-Unicode-Normalize}

Name:           %{?scl_prefix}perl-Unicode-Normalize
Version:        1.25
Release:        366%{?dist}
Summary:        Unicode Normalization Forms
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Unicode-Normalize/
Source0:        http://www.cpan.org/authors/id/K/KH/KHW/Unicode-Normalize-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl-libs
BuildRequires:  %{?scl_prefix}perl-libs
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(SelectSaver)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

%{?perl_default_filter}

%description
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.

%prep
%setup -q -n Unicode-Normalize-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.25-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Petr Šabata <contyk@redhat.com> - 1.25-1
- 1.25 bump

* Thu Dec 03 2015 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Tue Oct 27 2015 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Thu Jul 02 2015 Petr Pisar <ppisar@redhat.com> 1.18-348
- Specfile autogenerated by cpanspec 1.78.
