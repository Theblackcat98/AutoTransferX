[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<a name="readme-top"></a>


<br /><div align="center">  <a href="https://github.com/theblackcat98/autotransferx">    <img src="images/logo.png" alt="Logo" width="80" height="80">  </a>

<h3 align="center">AutoTransferX</h3>
<h3 align="center">[https://img.shields.io/badge/BlackCat-Designs-blueviolet]</h3>


<p align="center">
    AutoTransfer is a lightweight and easy-to-use program designed to automatically transfer files between folders based on their file extension. Simply specify a source folder to watch and a destination folder to transfer files to, and AutoTransfer will do the rest. With support for multiple file extensions and the ability to customize transfer settings, AutoTransfer makes it easy to manage and organize your files without manual intervention. Whether you're a developer looking to automate file transfers for a project or a user looking to simplify your file management process, AutoTransfer is the perfect solution.
    <br />
    <a href="https://github.com/theblackcat98/autotransferx"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/theblackcat98/AutoTransferX">View Demo</a>
    ·
    <a href="https://github.com/theblackcat98/AutoTransferX/issues">Report Bug</a>
    ·
    <a href="https://github.com/theblackcat98/AutoTransferX/issues">Request Feature</a>
  </p>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

Features:

- Automatically transfer files based on their extension
- Watch a folder and transfer files as soon as they are added
- Support for any file extension
- [ ] Customize transfer settings, including file overwrite rules and file renaming options
- Lightweight and easy-to-use CLI
- [ ] Cross-platform compatibility (macOS, Linux)
- **Open-source and free to use**

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Make sure to have `Python` installed on your device, then,
to get a local copy up and running follow these steps.

### Installation

1. Clone the repo
   
   ```sh
   git clone https://github.com/theblackcat98/AutoTransferX.git
   ```

2. Open `main.py`, and follow the CLI to create your first folder pair!

    ```sh
    ./main.py
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The specified watch folder is the Downloads folder, and the Documents folder as the destination folder to transfer files to. The user has also specified two different file extensions to watch for - ".pdf" and ".docx".

When a new file with one of these extensions is added to the Downloads folder, AutoTransfer automatically transfers it to the corresponding subfolder in the Documents folder. For example, a new PDF file is transferred to the Documents/PDFs folder, and a new Word document is transferred to the Documents/Word Docs folder. This saves the user time and effort by organizing their files automatically based on their file type.

_For more examples, please refer to the [Documentation](https://example.com)_ (todo)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Customize transfer settings
  - [ ] Regex support
  - [ ] File overwrite rules
  - [ ] File renaming options
- [ ] Folder Pair Database
  - [ ] folder_pair_db.json: Json file to store and manipulate the folder pairs' settings, names, info etc.
- [ ] Better GUI
- [ ] Packaging
  - [ ] `.exe` App
  - [ ] `.dmg` App
  - [ ] Linux??

See the [open issues](https://github.com/theblackcat98/AutoTransferX/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - email@email_client.com

Project Link: [https://github.com/theblackcat98/AutoTransferX](https://github.com/theblackcat98/AutoTransferX)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


##### App Layout

GUI

gui.py: Contains the main GUI class FileTransferGUI with methods for displaying the UI elements and handling user events.

File Transfer

file_transfer.py: Contains the FileTransfer class that handles the file transfer functionality.

Logging

logger.py: Contains the Logger class that handles logging of events.

Utility

utils.py: Contains any utility functions that are needed across multiple modules.

Main

main.py: The main entry point of the application, where the classes and modules are instantiated and executed.

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/theblackcat98/AutoTransferX.svg?style=flat&logo=appveyor

[forks-url]: https://github.com/theblackcat98/AutoTransferX/network/members

[stars-shield]: https://img.shields.io/github/stars/theblackcat98/AutoTransferX.svg?style=flat&logo=appveyor

[stars-url]: https://github.com/theblackcat98/AutoTransferX/stargazers

[issues-shield]: https://img.shields.io/github/issues/theblackcat98/AutoTransferX.svg?style=flat&logo=appveyor

[issues-url]: https://github.com/theblackcat98/AutoTransferX/issues

[license-shield]: https://img.shields.io/github/license/theblackcat98/AutoTransferX.svg?style=flat&logo=appveyor

[license-url]: https://github.com/theblackcat98/AutoTransferX/blob/master/LICENSE.txt
