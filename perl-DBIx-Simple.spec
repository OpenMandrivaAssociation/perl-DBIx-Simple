
%define realname   DBIx-Simple
%define version    1.32
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Easy-to-use OO interface to DBI
Source:     http://www.cpan.org/modules/by-module/DBIx/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(DBI)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



