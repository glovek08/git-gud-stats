<script lang="ts">
  import { Footer, FooterCopyright, FooterLinkGroup,
    FooterLink, FooterIcon, } from "flowbite-svelte";
  import { FacebookSolid, GithubSolid, DiscordSolid, TwitterSolid, } from "flowbite-svelte-icons";
  import logoDark from "$lib/assets/GitGudStats_logo_dark.svg";
  import logoLight from "$lib/assets/GitGudStats_logo_light.svg";
</script>

<Footer footerType="socialmedia">
  <div class="md:flex md:justify-between">
    <div class="mb-6 md:mb-0">
      <a href="/" class="flex items-center">
        <img src={logoDark} class="mr-3 h-8 dark:hidden" alt="GitGudStats Logo" />
        <img src={logoLight} class="mr-3 h-8 hidden dark:block" alt="GitGudStats Logo" />
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">GitGudStats</span>
      </a>
    </div>
    <div class="gap-8 sm:gap-6 grid grid-cols-2 sm:grid-cols-3">
      <div><h2 class="mb-6 font-semibold text-gray-900 dark:text-white text-sm uppercase">
          Resources
        </h2>
        <FooterLinkGroup>
          <FooterLink class="mb-4" href="/">Flowbite</FooterLink>
          <FooterLink class="mb-4" href="/">Tailwind CSS</FooterLink>
        </FooterLinkGroup>
      </div>
      <div>
        <h2
          class="mb-6 font-semibold text-gray-900 dark:text-white text-sm uppercase"
        >
          Follow us
        </h2>
        <FooterLinkGroup>
          <FooterLink class="mb-4" href="/">GitHub</FooterLink>
          <FooterLink class="mb-4" href="/">Discord</FooterLink>
        </FooterLinkGroup>
      </div>
      <div>
        <h2
          class="mb-6 font-semibold text-gray-900 dark:text-white text-sm uppercase"
        >
          Legal
        </h2>
        <FooterLinkGroup>
          <FooterLink class="mb-4" href="/">Privacy Policy</FooterLink>
          <FooterLink class="mb-4" href="/">Terms & Conditions</FooterLink>
        </FooterLinkGroup>
      </div>
    </div>
  </div>
  <hr class="sm:mx-auto my-6 lg:my-8 border-gray-200 dark:border-gray-700" />
  <div class="sm:flex sm:justify-between sm:items-center">
    <FooterCopyright href="/" by="Flowbite™" />
    <div
      class="flex sm:justify-center space-x-6 rtl:space-x-reverse mt-4 sm:mt-0"
    >
      <FooterIcon href="/">
        <FacebookSolid
          class="w-5 h-5 text-gray-500 hover:text-gray-900 dark:hover:text-white dark:text-gray-500"
        />
      </FooterIcon>
      <FooterIcon href="/">
        <DiscordSolid
          class="w-5 h-5 text-gray-500 hover:text-gray-900 dark:hover:text-white dark:text-gray-500"
        />
      </FooterIcon>
      <FooterIcon href="/">
        <TwitterSolid
          class="w-5 h-5 text-gray-500 hover:text-gray-900 dark:hover:text-white dark:text-gray-500"
        />
      </FooterIcon>
      <FooterIcon href="/">
        <GithubSolid
          class="w-5 h-5 text-gray-500 hover:text-gray-900 dark:hover:text-white dark:text-gray-500"
        />
      </FooterIcon>
    </div>
  </div>
</Footer>
