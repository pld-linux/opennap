Summary:     	OpenNap is an Open Source effort to create a version of the proprietary Napster server. 
Summary(pl): 	OpenNap jest alternatyw� komercyjnego serwera napster, jednak�e dost�pn� ze �r�d�ami.
Name:        	opennap
Version:     	0.41
Release:     	1
Group:       	Networking/Daemons
Group(pl):   	Sieciowe/Serwery
Copyright:   	GPL
URL:         	http://prdownloads.sourceforge.net/opennap/%{name}-%{version}.tar.gz
Source:      	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Napster is a protocol for sharing files between users. With Napster, 
the files stay on the client machine, never passing through the server. 
The server provides the ability to search for particular files and
initiate a direct transfer between the clients. In addition, chat
forums similar to IRC are available. OpenNap extends the Napster 
protocol to allow sharing of any media type, and the ability to 
link servers together. 

%description -l pl
Napster jest protoko�em wsp�dzielenia plik�w. Napster pliki pozostawia
u ko�cowych u�ytkownik�w, nigdy fizycznie nie przebywaj� na serwerze.
Serwer umo�liwia jedynie wyszukiwanie konkretnych plik�w i inicjuje
bezpo�redni transfer pomi�dzy u�ytkownikami. Na dodatek zapewnia
komunikacj� podobn� do IRCa. OpenNap rozszerza protok� napstera 
o mo�liwo�� wsp�dzielenia ka�dego rodzaju plik�w oraz o mo�liwo��
po��cze� mi�dzyserwerowych.

%prep

%setup -q

%build
%configure \
	--prefix=/usr \
	--with-uid=opennap \
	--with-gid=opennap

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_datadir}
install -s metaserver opennap $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf AUTHORS NEWS README ChangeLog FAQ

%files
%defattr(644,opennap,opennap,700)
%attr(755,root,root) %{_sbindir}/*
#%attr(600,opennap,opennap) %{_datadir}/*

%doc *.gz

%clean
rm -rf $RPM_BUILD_ROOT
