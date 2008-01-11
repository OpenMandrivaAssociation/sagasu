%define version	2.0.8
%define release %mkrel 2

Name: 	 	sagasu
Summary: 	GNOME text searching tool
Version: 	%{version}
Release: 	%{release}
# http://www3.sympatico.ca/sarrazip/dev/sagasu-%{version}.tar.gz
Source:		%{name}-%{version}.tar.bz2
URL:		http://www3.sympatico.ca/sarrazip/dev/sagasu.html
License:	GPL
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeui2-devel bison
BuildRequires:	ImageMagick desktop-file-utils

%description
Sagasu is a GNOME tool to find strings in multiple files. The user specifies
the search directory and the set of files to be searched. Double-clicking on
a search result launches a user command that can for example load the file in
an editor at the appropriate line. The search can optionally ignore CVS
directories. Sagasu is a Japanese word that means "to search."

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Accessories" \
  --add-category="Development" \
  --add-category="Profiling" \
  --add-category="X-Mandrakelinux-MoreApplications-Development-Tools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


#icons
mkdir -p $RPM_BUILD_ROOT%{_iconsdir} \
         $RPM_BUILD_ROOT%{_miconsdir}
install -D -m 0644      src/images/sagasu.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -geometry 32x32 src/images/sagasu.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -geometry 16x16 src/images/sagasu.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_mandir}/man?/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

