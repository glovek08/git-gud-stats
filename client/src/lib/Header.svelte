<script lang="ts">
  import { Navbar, DarkMode, NavBrand, NavLi, NavUl, NavHamburger, Avatar,
    Dropdown, DropdownItem, DropdownHeader, DropdownGroup, } from "flowbite-svelte";
  //const currentFavicon = $derived($theme === 'dark' ? favicon_light : favicon_dark);
  import logoDark from "$lib/assets/GitGudStats_logo_dark.svg";
  import logoLight from "$lib/assets/GitGudStats_logo_light.svg";
</script>

<Navbar class="p-5 bg-white dark:bg-amber-50">
  <NavBrand href="/">
    <img src={logoDark} class="h-6 sm:h-9 dark:hidden" alt="GitGudStats Logo" />
    <img src={logoLight} class="h-6 sm:h-9 hidden dark:block" alt="GitGudStats Logo" />
    <span class="self-center font-semibold dark:text-fg text-xl whitespace-nowrap ml-3">GitGudStats</span>
  </NavBrand>
  <div class="flex items-center md:order-2">
    <Avatar
      id="avatar-menu"
      src="/user_pfp.jpeg"
      class="hover:cursor-pointer"
    />
    <!-- <NavHamburger /> This will display the NavUl -->
  </div>
  <DarkMode class="mr-5 ml-auto hover:cursor-pointer"></DarkMode>
  <Dropdown placement="bottom" triggeredBy="#avatar-menu">
    <DropdownHeader class="hover:cursor-pointer">
      <span class="block text-sm">Pepe Gutierrez</span>
      <span class="block font-medium text-sm truncate">pepe81</span>
    </DropdownHeader>
    <DropdownGroup>
      <DropdownItem>Charts</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Legal</DropdownItem>
    </DropdownGroup>
    <DropdownHeader>Sign out</DropdownHeader>
  </Dropdown>
  <!-- <NavUl> These are header buttons, leave them just in case you want to reimplement them.
    <NavLi href="/">Home</NavLi>
    <NavLi href="/about">About</NavLi>
    <NavLi href="/docs/components/navbar">Navbar</NavLi>
    <NavLi href="/pricing">Pricing</NavLi>
    <NavLi href="/contact">Contact</NavLi>
  </NavUl> -->
</Navbar>
