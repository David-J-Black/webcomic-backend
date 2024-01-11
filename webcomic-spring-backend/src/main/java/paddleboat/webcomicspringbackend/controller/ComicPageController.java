package paddleboat.webcomicspringbackend.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import paddleboat.webcomicspringbackend.model.system.AbstractBaseResource;
import paddleboat.webcomicspringbackend.model.PageIndex;
import paddleboat.webcomicspringbackend.service.ComicPageService;

@RestController
@RequestMapping("/page")
@RequiredArgsConstructor
@Slf4j
public class ComicPageController extends AbstractBaseResource {

    private final ComicPageService comicPageService;

    @GetMapping("/{chapterNumber}/{pageNumber}")
    public ResponseEntity<byte[]> getComicPage(@PathVariable Integer chapterNumber, @PathVariable Integer pageNumber) throws Exception {
        try {
            PageIndex pageIndex = new PageIndex(chapterNumber, pageNumber);
            return success(comicPageService.getComicPageImage(pageIndex));
        } catch( Exception e) {
            log.error("Exception getting page image!", e);
            throw e;
        }
    }
}
