package paddleboat.webcomicspringbackend.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import paddleboat.webcomicspringbackend.model.system.AbstractBaseResource;
import paddleboat.webcomicspringbackend.service.cache.ComicCache;

/**
 * The CacheController class provides REST endpoints to manage the data_caches
 */
@RestController
@RequestMapping("/cache")
@RequiredArgsConstructor
@Slf4j
public class CacheController extends AbstractBaseResource {

    private final ComicCache comicCache;


    @GetMapping("")
    public ResponseEntity<Integer> refreshCaches() {
        try {
            return success(comicCache.load());
        } catch( Exception e) {
            log.error("Exception getting page image!", e);
            throw e;
        }
    }
}
