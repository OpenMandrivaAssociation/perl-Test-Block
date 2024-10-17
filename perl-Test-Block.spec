%define upstream_name    Test-Block
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.13
Release:	3

Summary:	Specify fine granularity test plans
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Block-0.13.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module allows you to specify the number of expected tests at a finer
level of granularity than an entire test script. It is built with the
Test::Builder manpage and plays happily with the Test::More manpage and
friends.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Test

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 664907
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 405545
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268730
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 213785
- import perl-Test-Block


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
- fist mdv release

