from numpy.random import randint

COOKIES: list[str] = [
    "Georges Melies",
    "Georges Melies",
    "Georges Melies",
    "Georges Melies",
    "James Clerk Maxwell",
    "James Clerk Maxwell",
    "James Clerk Maxwell",
    "Mary Antoinette",
    "Mark Twain",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Lego Man #7",
    "Lego Man #3",
]


class CookieElf:
    def om_nom_eat_them_cookies(self, cookies: list[str]) -> None:
        self.cookies: list[str] = cookies
        self.plebians: dict[str, int] = dict({plebian : self.cookies.count(plebian) for plebian in set(cookies)})
        self.plebians = dict(sorted(self.plebians.items()))  # sort the dict by those with the most cookies

    def dictate(self) -> dict[str, list[str]]:
        decree: dict[str, list[str]] = {plebian : [] for plebian in self.plebians.keys()}
        for plebian in self.plebians.keys():
            n_cookies = self.plebians[plebian]
            for cookie_eater in self.plebians.keys():
                if n_cookies == 0:
                    break
                if cookie_eater != plebian:
                    decree[cookie_eater].append(plebian)
                    n_cookies -= 1
            if n_cookies != 0:
                raise RuntimeError("Not a valid cookie pattern!")
        return decree
    
if __name__ == "__main__":
    the_elf = CookieElf()
    the_elf.om_nom_eat_them_cookies(COOKIES)
    decree = the_elf.dictate()
    print("🎄 Thus sayeth the master elf! Hear ye! Hear YE! 🎄")
    for plebian, cookies in decree.items():
        print(f"Unto {plebian} is assigned the following:")
        for cookie in cookies:
            print(f" - {cookie}")
    print("This concludes my proclaimation. May the snow fall gently on your visiage ❄️")