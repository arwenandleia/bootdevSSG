import unittest
from extract_markdown_images import extract_markdown_images,extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_bd_ex_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        md_image_list = extract_markdown_images(text)
        self.assertListEqual(
            md_image_list,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ])
        
    def test_empty_alt_text(self):
        text = "No alt text here ![](https://i.imgur.com/aKaOqIh.gif) "
        md_image_list = extract_markdown_images(text)
        self.assertListEqual(
            md_image_list,
            [
                ("", "https://i.imgur.com/aKaOqIh.gif"), 
                ])
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_empty_text(self):
        text = 'No imags here'
        md_image_list = extract_markdown_images(text)
        self.assertListEqual(
            md_image_list,
            []
            )
        


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_bd_ex_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        md_link_list = extract_markdown_links(text)
        self.assertListEqual(
            md_link_list,
            [
                ("to boot dev", "https://www.boot.dev"), 
                ("to youtube", "https://www.youtube.com/@bootdotdev")
                ])
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

        


    