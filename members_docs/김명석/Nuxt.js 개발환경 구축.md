1. npm 버전 5.2.0 이상이면 npx가 기본적으로 설치 되어있음

    ```bash
    $ npx -v
    6.14.5
    ```

    ```bash
    $ npm -v
    6.14.5
    ```

2. nuxt.js 프로젝트 생성

    ```bash
    $ npx create-nuxt-app frontend

    create-nuxt-app v3.2.0
    ✨  Generating Nuxt.js project in frontend

    2-1. 프로젝트 이름 정하기
    ? Project name: ZIP-Children

    2-2. 사용할 언어
    ? Programming language: (Use arrow keys)
    > JavaScript
      TypeScript

    2-3. Package Manager는 무엇을 쓸것인가?
    ? Choose the package manager <Npm>
      Yarn
    > Npm

    2-4. UI framework를 사용할 것인가? 사용한다면 어떤것을 사용할것인가?
    ? Choose UI framework <None>
    > None
      Ant Design Vue
      Bootstrap Vue
      Buefy
      Bulma
      Element
      Framevuerk
      iView
      Tachyons
      Tailwind CSS
      Vuesax
      Vuetify.js

    2-5. Nuxt.js Module을 사용할 것인가? (axios를 사용하기 때문에 space 키를 눌러 설정해주었다.) 
    ? Choose Nuxt.js modules (Press <space> to select, <a> to toggle all, <i> to invert selection)
    >(*) Axios
     ( ) Progressive Web App (PWA) Support
     ( ) DotEnv       

    2-6. linting tools를 사용할 것인가? (ESLint를 사용하기 때문에 space 키를 눌러 설정해주었다.)
    ? Choose linting tools (Press <space> to select, <a> to toggle all, <i> to invert selection)
    (*) ESLint
    ( ) Prettier
    ( ) Lint staged files
    ( ) StyleLint 

    2-7. test framework를 사용할 것인가? 사용한다면 어떤것을 사용할것인가?
    ? Choose test framework <None>
    > None
      Jest
      AVA

    2-8. 렌더링 모드를 선택해라. 
    ? Choose rendering mode <Single Page App>
      Universal (SSR)
    > Single Page App

    2-9. 배포 대상
    ? Deployment target: (Use arrow keys)
      Server (Node.js hosting) 서버 측 렌더링 용
    > Static (Static/JAMStack hosting) 정적 사이트 용

    2-10. 개발 환경
    ? Development tools:
    >(*) jsconfig.json (Recommended for VS Code if you're not using typescript)
     ( ) Semant/ic Pull Requests

    \ Installing packages with npm
    ...
    ...
    ...

    설치중

    ...
    ...
    ...

    �  Successfully created project ZIP-Children

      To get started:

            cd frontend
            npm run dev

      To build & start for production:

            cd frontend
            npm run build
            npm run start

    한 1~2분 정도 걸린듯
    ```

3. 실행 해보기

    ```bash
    np$ npm run dev

    > ZIP-Children@1.0.0 dev C:\Users\multicampus\Desktop\SSAFY\gitlab\PJT2\frontend
    > nuxt

    i NuxtJS collects completely anonymous data about usage.                                                                                                               20:57:35
      This will help us improving Nuxt developer experience over the time.
      Read more on https://git.io/nuxt-telemetry

    ? Are you interested in participation? (Y/n) n
    뭐 개발에 참여 의향 물어보는거같은데 그냥 아무거나 해도댐

       ╭───────────────────────────────────────╮
       │                                       │
       │   Nuxt.js @ v2.14.4                   │
       │                                       │
       │   ▸ Environment: development          │
       │   ▸ Rendering:   client-side          │
       │   ▸ Target:      static               │
       │                                       │
       │   Listening: http://localhost:3000/   │
       │                                       │
       ╰───────────────────────────────────────╯

    i Preparing project for development                                                                                                                                    20:58:48
    i Initial build may take a while                                                                                                                                       20:58:48
    √ Builder initialized                                                                                                                                                  20:58:48
    √ Nuxt files generated                                                                                                                                                 20:58:48

    √ Client
      Compiled successfully in 5.21s

    i Waiting for file changes                                                                                                                                             20:58:54
    i Memory usage: 214 MB (RSS: 282 MB)                                                                                                                                   20:58:54  
    i Listening on: http://localhost:3000/

    스근하게 실행해보기
    ```

4. 아래로 접속 시작

    [](http://localhost:3000/)

5. 확인