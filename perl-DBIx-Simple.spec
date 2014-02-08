%define	module	DBIx-Simple
%define	modver	1.35

Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	10

Summary:	Easy-to-use OO interface to DBI
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{module}-%{modver}.tar.gz

BuildRequires:	perl(DBI)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

This module is aimed at rapid development and easy maintenance. Query
preparation and execution are combined in a single method, the result
object (which is a wrapper around the statement handle) provides easy
row-by-row and slurping methods.

The 'query' method returns either a result object, or a dummy object. The
dummy object returns undef (or an empty list) for all methods and when used
in boolean context, is false. The dummy object lets you postpone (or skip)
error checking, but it also makes immediate error checking simply
'$db->query(...) or die $db->error'.

%prep
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.350.0-8
- rebuild for perl-5.16.2
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.350.0-6mdv2012.0
+ Revision: 765166
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.350.0-4
+ Revision: 763239
- force it
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.350.0-3
+ Revision: 657771
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.350.0-1mdv2011.0
+ Revision: 628708
- update to new version 1.35

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.340.0-1mdv2011.0
+ Revision: 622680
- update to new version 1.34

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1mdv2011.0
+ Revision: 612075
- update to new version 1.33

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2011.0
+ Revision: 401669
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.32-1mdv2010.0
+ Revision: 375954
- import perl-DBIx-Simple


